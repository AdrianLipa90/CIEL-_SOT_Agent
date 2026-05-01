# ciel_doc_ingest.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/ciel_doc_ingest.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/ciel_doc_ingest.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _apply_heisenberg_clip, _parse_txt, _parse_md, _parse_pdf, _parse_docx, _parse_file, _chunk_text, _write_chunks_to_tsm, _update_encoder, ingest_file, ingest_directory

## Docstring
CIEL Document Ingestor — PDF / DOCX / MD / TXT → BlochEncoder online update.

Parsuje dokumenty, segmentuje na chunki, wpina w online_update BlochEncodera.
Każdy chunk = jeden tekst do nauki. Chunki są też zapisywane do TSM jako
nowe wpisy pamięci (D_type='document').

Użycie:
    python -m ciel_doc
