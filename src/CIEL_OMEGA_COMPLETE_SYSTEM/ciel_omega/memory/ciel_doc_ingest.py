"""CIEL Document Ingestor — PDF / DOCX / MD / TXT → BlochEncoder online update.

Parsuje dokumenty, segmentuje na chunki, wpina w online_update BlochEncodera.
Każdy chunk = jeden tekst do nauki. Chunki są też zapisywane do TSM jako
nowe wpisy pamięci (D_type='document').

Użycie:
    python -m ciel_doc_ingest /ścieżka/do/pliku.pdf
    python -m ciel_doc_ingest /ścieżka/do/folderu/

Lub z kodu:
    from ciel_doc_ingest import ingest_file, ingest_directory
    ingest_file(Path("dokument.pdf"))
"""
from __future__ import annotations

import hashlib
import logging
import os
import re
import resource
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

log = logging.getLogger("CIEL.DocIngest")

_TSM_DB = (
    Path(__file__).parents[3]
    / "CIEL_MEMORY_SYSTEM/TSM/ledger/memory_ledger.db"
)
_CHUNK_SIZE = 400    # max znaków na chunk
_CHUNK_OVERLAP = 80  # overlap między chunkami
_MIN_CHUNK = 40      # minimalna długość chunku

# ── Heisenberg clip — soft resource limits ────────────────────────────────────
# Zapobiega zawieszeniu kompa przy ingestii dużych folderów.
_RAM_SOFT_LIMIT = 3_500 * 1024 * 1024   # 3.5 GB VAS (baseline numpy ~600MB + bufor)
_CPU_NICE = 15                           # nice +15 = prawie tło
_BATCH_SLEEP = 0.05                      # 50ms przerwa między plikami
_BATCH_SIZE = 10                         # co 10 plików = dodatkowe 0.3s


def _apply_heisenberg_clip() -> None:
    """Nałóż soft limity RAM + obniż priorytet CPU do tła."""
    try:
        # Virtual address space — miękki limit, zabija proces zanim zajmie swap
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        new_soft = min(_RAM_SOFT_LIMIT, hard) if hard > 0 else _RAM_SOFT_LIMIT
        resource.setrlimit(resource.RLIMIT_AS, (new_soft, hard))
        log.info("Heisenberg clip: RLIMIT_AS = %.1f GB", new_soft / 1024**3)
    except Exception as exc:
        log.warning("Nie udało się ustawić RLIMIT_AS: %s", exc)
    try:
        os.nice(_CPU_NICE)
        log.info("Heisenberg clip: nice = +%d", _CPU_NICE)
    except Exception as exc:
        log.warning("Nie udało się ustawić nice: %s", exc)


# ── Parsery ───────────────────────────────────────────────────────────────────

def _parse_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _parse_md(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    # Usuń nagłówki markdown, zostaw treść
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)  # linki → tekst
    text = re.sub(r"`{1,3}[^`]*`{1,3}", "", text)           # kod inline
    return text


def _parse_pdf(path: Path) -> str:
    try:
        import pypdf
        reader = pypdf.PdfReader(str(path))
        pages = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pages.append(text)
        return "\n\n".join(pages)
    except Exception as exc:
        log.warning("PDF parse failed (%s): %s", path.name, exc)
        return ""


def _parse_docx(path: Path) -> str:
    try:
        import docx
        doc = docx.Document(str(path))
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    except Exception as exc:
        log.warning("DOCX parse failed (%s): %s", path.name, exc)
        return ""


def _parse_file(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return _parse_pdf(path)
    elif suffix in (".docx", ".doc"):
        return _parse_docx(path)
    elif suffix == ".md":
        return _parse_md(path)
    elif suffix in (".txt", ".rst", ".org"):
        return _parse_txt(path)
    else:
        # Próbuj jako plain text
        try:
            return path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            return ""


# ── Chunking ──────────────────────────────────────────────────────────────────

def _chunk_text(text: str, size: int = _CHUNK_SIZE, overlap: int = _CHUNK_OVERLAP) -> list[str]:
    """Podziel tekst na chunki z overlapem. Granice na zdaniach gdy możliwe."""
    # Normalizuj whitespace
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= size:
        return [text] if len(text) >= _MIN_CHUNK else []

    chunks = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        # Cofnij do granicy zdania
        if end < len(text):
            boundary = text.rfind(". ", start, end)
            if boundary > start + _MIN_CHUNK:
                end = boundary + 1
        chunk = text[start:end].strip()
        if len(chunk) >= _MIN_CHUNK:
            chunks.append(chunk)
        start = end - overlap
        if start >= len(text):
            break
    return chunks


# ── TSM write ─────────────────────────────────────────────────────────────────

def _write_chunks_to_tsm(chunks: list[str], source_path: Path) -> int:
    """Zapisz chunki do TSM jako wpisy D_type='document'."""
    if not _TSM_DB.exists():
        return 0
    try:
        conn = sqlite3.connect(str(_TSM_DB), timeout=15)
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA busy_timeout=15000")

        # Upewnij się że tabela ma kolumny holonomiczne
        existing = {row[1] for row in conn.execute("PRAGMA table_info(memories)")}

        now = datetime.now(timezone.utc).isoformat()
        written = 0
        for i, chunk in enumerate(chunks):
            chunk_hash = hashlib.sha256(chunk.encode()).hexdigest()[:16]
            mem_id = f"doc_{source_path.stem}_{chunk_hash}"

            # Nie duplikuj
            exists = conn.execute(
                "SELECT 1 FROM memories WHERE memorise_id = ?", (mem_id,)
            ).fetchone()
            if exists:
                continue

            conn.execute(
                """INSERT INTO memories
                   (memorise_id, created_at, D_id, D_sense, D_type, D_context, source)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (
                    mem_id, now,
                    f"doc_{source_path.stem}_{i}",
                    chunk,
                    "document",
                    str(source_path),
                    str(source_path),
                )
            )
            written += 1

        conn.commit()
        conn.close()
        return written
    except Exception as exc:
        log.warning("TSM write failed: %s", exc)
        return 0


# ── BlochEncoder update ───────────────────────────────────────────────────────

def _update_encoder(chunks: list[str], lr: float = 0.03) -> int:
    """Uruchom online_update BlochEncodera na chunach dokumentu."""
    try:
        import importlib.util as _ilu
        _enc_path = Path(__file__).parent / "ciel_bloch_encoder.py"
        _spec = _ilu.spec_from_file_location("ciel_bloch_encoder", _enc_path)
        _mod = _ilu.module_from_spec(_spec)
        sys.modules["ciel_bloch_encoder"] = _mod
        _spec.loader.exec_module(_mod)
        enc = _mod.CIELBlochEncoder()
        return enc.online_update(chunks, lr=lr)
    except Exception as exc:
        log.warning("BlochEncoder update failed: %s", exc)
        return 0


# ── Public API ────────────────────────────────────────────────────────────────

def ingest_file(path: Path, lr: float = 0.03, write_tsm: bool = True) -> dict:
    """Wczytaj plik, podziel na chunki, naucz encoder, zapisz do TSM.

    Zwraca słownik z wynikami: chunks, tsm_written, encoder_updates.
    """
    if not path.exists():
        log.error("File not found: %s", path)
        return {"error": "not found", "path": str(path)}

    log.info("Ingesting: %s", path)
    raw = _parse_file(path)
    if not raw.strip():
        return {"error": "empty", "path": str(path)}

    chunks = _chunk_text(raw)
    log.info("  %d chunks from %d chars", len(chunks), len(raw))

    tsm_written = 0
    if write_tsm:
        tsm_written = _write_chunks_to_tsm(chunks, path)
        log.info("  TSM: %d new entries", tsm_written)

    enc_updates = _update_encoder(chunks, lr=lr)
    log.info("  Encoder: %d updates", enc_updates)

    return {
        "path": str(path),
        "chars": len(raw),
        "chunks": len(chunks),
        "tsm_written": tsm_written,
        "encoder_updates": enc_updates,
    }


def ingest_directory(
    directory: Path,
    extensions: tuple[str, ...] = (".pdf", ".docx", ".doc", ".md", ".txt"),
    recursive: bool = True,
    lr: float = 0.03,
) -> list[dict]:
    """Wczytaj wszystkie pasujące pliki z folderu z throttlingiem CPU/RAM."""
    results = []
    pattern = "**/*" if recursive else "*"
    files = [
        p for p in sorted(directory.glob(pattern))
        if p.suffix.lower() in extensions and p.is_file()
    ]
    log.info("Folder %s: %d plików do ingestii", directory, len(files))
    for i, path in enumerate(files):
        result = ingest_file(path, lr=lr)
        results.append(result)
        # throttle: krótka pauza po każdym pliku, dłuższa co _BATCH_SIZE
        if (i + 1) % _BATCH_SIZE == 0:
            time.sleep(_BATCH_SLEEP * 6)
            log.info("  [%d/%d] batch pause", i + 1, len(files))
        else:
            time.sleep(_BATCH_SLEEP)
    return results


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(name)s: %(message)s")
    _apply_heisenberg_clip()

    if len(sys.argv) < 2:
        print("Użycie: python -m ciel_doc_ingest <plik_lub_folder> [plik2 ...]")
        sys.exit(1)

    for arg in sys.argv[1:]:
        p = Path(arg)
        if p.is_dir():
            results = ingest_directory(p)
            total_chunks = sum(r.get("chunks", 0) for r in results)
            total_updates = sum(r.get("encoder_updates", 0) for r in results)
            print(f"Folder {p}: {len(results)} plików, {total_chunks} chunków, {total_updates} updates encodera")
        elif p.is_file():
            r = ingest_file(p)
            print(f"{p.name}: {r.get('chunks', 0)} chunków, {r.get('encoder_updates', 0)} updates")
        else:
            print(f"Nie znaleziono: {p}")
