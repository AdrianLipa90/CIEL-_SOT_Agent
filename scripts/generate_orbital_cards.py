#!/usr/bin/env python3
"""Generator kart orbitalnych — każdy obiekt w każdej bazie dostaje kartę z M_sem.

Semantyczny Collatz + Zeta-Schrödinger = M_sem, nie hash, nie rozmiar pliku.
Każda karta zawiera:
  - M_sem, M_EC, M_ZS, C_dep, C_prov, C_exec
  - orbit_period, orbit_radius
  - attractor_sector — który z 10 centroidów WΩ jest jego atraktorem

Źródła obiektów:
  TSM          → każdy rekord memories (D_type, D_sense, phi_berry, winding_n)
  GLOSSARY     → każda karta (symbol, name, card_type, formula)
  REG_SECTORS  → każdy sektor orbitalny
  REG_ENTITIES → każda encja (ciel_entity_cards.yaml)
  REG_REPOS    → każde repozytorium
  REG_WORDS    → każda karta słowa

Output: docs/object_cards/db/<source>/<id>.md
Index:  docs/object_cards/db/INDEX.md

Użycie:
    python scripts/generate_orbital_cards.py          # wszystkie źródła
    python scripts/generate_orbital_cards.py tsm      # tylko TSM
    python scripts/generate_orbital_cards.py glossary sectors entities repos
"""
from __future__ import annotations

import json
import math
import re
import sqlite3
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO = Path(__file__).parent.parent
SRC  = REPO / "src"
INTG = REPO / "integration"
OUT  = REPO / "docs" / "object_cards" / "db"
OUT.mkdir(parents=True, exist_ok=True)

# ── Paths ────────────────────────────────────────────────────────────────────

_PATHS = {
    "tsm":      REPO / "src/CIEL_OMEGA_COMPLETE_SYSTEM/CIEL_MEMORY_SYSTEM/TSM/ledger/memory_ledger.db",
    "glossary": REPO / "src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary/generated/ciel_semantic_glossary.db",
    "wo":       REPO / "src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/bloch_weights.npz",
    "sectors":  INTG / "Orbital/main/manifests/sectors_global.json",
    "couplings":INTG / "Orbital/main/manifests/couplings_global.json",
    "entities": INTG / "registries/ciel_entity_cards.yaml",
    "repos":    INTG / "registries/repository_registry.json",
    "words":    INTG / "registries/words/word_cards_registry.json",
}

# ── M_sem weights (RELATIONAL_SEED_ORBIT_SOLVER_V0) ──────────────────────────

_ALPHA = 0.30
_BETA  = 0.25
_CHI   = 0.20
_DELTA = 0.15
_EPS   = 0.10
_TAU_REF = 0.489

_HORIZON_DEPTH = {
    "SEALED": 1.0, "TRANSMISSIVE": 0.80, "POROUS": 0.65, "OBSERVATIONAL": 0.35,
}
_TYPE_PROV = {
    "ethical_anchor": 1.0, "identity": 0.85, "episodic": 0.65,
    "procedural": 0.55, "document": 0.45, "text": 0.40,
}
_ROLE_PROV = {
    "canonical-foundations": 1.0, "integration-attractor": 0.90,
    "historical-theory-simulations": 0.75, "desktop-runtime-surface": 0.65,
    "cockpit-ui-education": 0.55,
}

# Sektory WΩ (kolejność zgodna z SECTORS w encoderze)
_WO_SECTORS = [
    "identity", "episodic", "procedural", "conceptual",
    "conflict", "meta", "project", "ethics", "temporal", "abstraction",
]


# ── Karta orbitalna ───────────────────────────────────────────────────────────

@dataclass
class OrbitalCard:
    obj_id: str          # unikalny id
    source: str          # tsm | glossary | sectors | entities | repos | words
    name: str
    M_sem: float
    M_EC: float
    M_ZS: float
    C_dep: float
    C_prov: float
    C_exec: float
    orbit_period: float
    orbit_radius: float
    attractor_sector: str   # sektor WΩ atraktora
    attractor_cos: float    # podobieństwo cosinusowe do atraktora
    phi: float = 0.0        # faza [0, 2π)
    theta: float = 0.0      # kąt polarny [0, π]
    extra: dict[str, Any] = None  # dodatkowe pola źródłowe

    def __post_init__(self):
        if self.extra is None:
            self.extra = {}


def _kepler(M_sem: float, a: float) -> tuple[float, float]:
    """T² ∝ a³ / M_sem → (T, a)"""
    a = max(1e-6, min(0.999, a))
    T = math.sqrt(a ** 3 / max(1e-9, M_sem))
    return round(T, 5), round(a, 5)


def _bloch_vec(theta: float, phi: float):
    import numpy as np
    return np.array([
        math.sin(theta) * math.cos(phi),
        math.sin(theta) * math.sin(phi),
        math.cos(theta),
    ], dtype=float)


def _find_attractor(theta: float, phi: float) -> tuple[str, float]:
    """Znajdź sektor WΩ najbliższy danemu stanowi Blocha."""
    try:
        import numpy as np
        wo_path = _PATHS["wo"]
        if wo_path.exists():
            WO = np.load(str(wo_path))["WO"]  # (10, 3)
        else:
            # Fallback: deterministyczne centroidy
            WO = np.zeros((10, 3), dtype=float)
            for i in range(10):
                t = math.pi * i / 10
                p = 2 * math.pi * i / 10
                WO[i] = [math.sin(t)*math.cos(p), math.sin(t)*math.sin(p), math.cos(t)]
        vec = _bloch_vec(theta, phi)
        norm = np.linalg.norm(vec)
        if norm > 1e-9:
            vec /= norm
        dots = WO @ vec
        k = int(np.argmax(dots))
        return _WO_SECTORS[k], round(float(dots[k]), 4)
    except Exception:
        return "conceptual", 0.0


# ── Źródła ────────────────────────────────────────────────────────────────────

def _load_tsm(limit: int = 500) -> list[OrbitalCard]:
    path = _PATHS["tsm"]
    if not path.exists():
        return []
    conn = sqlite3.connect(str(path), timeout=10)
    conn.execute("PRAGMA journal_mode=WAL")
    rows = conn.execute(
        "SELECT memorise_id, D_sense, D_type, phi_berry, winding_n, D_context "
        "FROM memories WHERE D_sense IS NOT NULL "
        "ORDER BY winding_n DESC NULLS LAST LIMIT ?", (limit,)
    ).fetchall()
    conn.close()

    cards = []
    for mem_id, sense, dtype, phi_berry, winding_n, ctx in rows:
        phi_b = float(phi_berry or 0.0)
        wn    = int(winding_n or 0)
        dtype = str(dtype or "text")

        # M_EC — Euler-Collatz: log1p(winding_n) / log1p(200)
        M_EC = math.log1p(wn) / math.log1p(200)
        # M_ZS — Zeta-Schrödinger: bliskość fazy do rezonansu
        gap  = min(abs(phi_b), abs(phi_b - 2 * math.pi))
        M_ZS = 1.0 - min(gap / math.pi, 1.0)
        # C_dep — typ wpisu
        C_dep  = _TYPE_PROV.get(dtype, 0.40)
        C_prov = _TYPE_PROV.get(dtype, 0.40)
        C_exec = min(1.0, wn / 50.0)

        M_sem = _ALPHA*M_EC + _BETA*M_ZS + _CHI*C_dep + _DELTA*C_prov + _EPS*C_exec

        phi   = phi_b % (2 * math.pi)
        theta = math.pi * (1.0 - min(M_sem, 1.0))
        a     = max(0.05, M_sem)
        T, a  = _kepler(M_sem, a)
        att, cos = _find_attractor(theta, phi)

        cards.append(OrbitalCard(
            obj_id=f"tsm:{mem_id}",
            source="tsm",
            name=str(sense or mem_id)[:80],
            M_sem=round(M_sem, 5), M_EC=round(M_EC, 5), M_ZS=round(M_ZS, 5),
            C_dep=round(C_dep, 5), C_prov=round(C_prov, 5), C_exec=round(C_exec, 5),
            orbit_period=T, orbit_radius=a,
            attractor_sector=att, attractor_cos=cos,
            phi=round(phi, 4), theta=round(theta, 4),
            extra={"dtype": dtype, "winding_n": wn, "phi_berry": phi_b, "context": (ctx or "")[:100]},
        ))
    return cards


def _load_glossary(limit: int = 200) -> list[OrbitalCard]:
    path = _PATHS["glossary"]
    if not path.exists():
        return []
    conn = sqlite3.connect(str(path), timeout=10)
    rows = conn.execute(
        "SELECT stable_id, symbol, name, card_type, numeric_value, formula "
        "FROM cards LIMIT ?", (limit,)
    ).fetchall()
    conn.close()

    cards = []
    for sid, symbol, name, ctype, nval, formula in rows:
        # M_EC z numeric_value (jeśli liczba → Collatz "odległość" od 1)
        nv = float(nval) if nval else 0.0
        # Collatz: log1p cyklu do 1 dla wartości całkowitych
        if nv > 0:
            collatz_steps = _collatz_steps(int(min(nv, 10000)))
            M_EC = math.log1p(collatz_steps) / math.log1p(100)
        else:
            M_EC = 0.3
        # M_ZS z nazwy karty (symbol analityczny → wyższy rezonans)
        M_ZS = 0.8 if formula else 0.5
        C_dep  = 0.7  # karty glossary są wewnętrznie spójne
        C_prov = {"operator": 0.9, "constant": 0.85, "metric": 0.8, "concept": 0.7}.get(ctype or "", 0.6)
        C_exec = 0.5 if formula else 0.3

        M_sem = _ALPHA*M_EC + _BETA*M_ZS + _CHI*C_dep + _DELTA*C_prov + _EPS*C_exec

        phi   = (hash(str(symbol or sid)) % 1000) / 1000 * 2 * math.pi
        theta = math.pi * (1.0 - min(M_sem, 1.0))
        T, a  = _kepler(M_sem, M_sem)
        att, cos = _find_attractor(theta, phi)

        cards.append(OrbitalCard(
            obj_id=f"glossary:{sid}",
            source="glossary",
            name=f"{symbol or sid} — {name or ''}".strip(" —"),
            M_sem=round(M_sem, 5), M_EC=round(M_EC, 5), M_ZS=round(M_ZS, 5),
            C_dep=round(C_dep, 5), C_prov=round(C_prov, 5), C_exec=round(C_exec, 5),
            orbit_period=T, orbit_radius=a,
            attractor_sector=att, attractor_cos=cos,
            phi=round(phi, 4), theta=round(theta, 4),
            extra={"card_type": ctype, "formula": formula or "", "numeric_value": nv},
        ))
    return cards


def _load_sectors() -> list[OrbitalCard]:
    path = _PATHS["sectors"]
    coup_path = _PATHS["couplings"]
    if not path.exists():
        return []
    raw = json.loads(path.read_text())
    couplings = {}
    if coup_path.exists():
        cr = json.loads(coup_path.read_text())
        couplings = cr.get("couplings", {})

    cards = []
    for name, s in raw.get("sectors", {}).items():
        info_mass = float(s.get("info_mass", 1.0))
        coh_w     = float(s.get("coherence_weight", 1.0))
        tau       = float(s.get("tau", 0.353))
        amplitude = float(s.get("amplitude", 1.0))
        theta_s   = float(s.get("theta", math.pi/4))
        phi_s     = float(s.get("phi", 0.0))
        coup_sum  = sum(float(v) for tgt, v in couplings.get(name, {}).items())

        M_EC  = info_mass * (0.5 + 0.5 * min(1.0, coup_sum))
        tau_n = tau / _TAU_REF
        M_ZS  = coh_w * (0.5 + 0.5 * tau_n)
        C_dep = min(1.0, coup_sum / 3.0)
        C_prov = amplitude
        C_exec = amplitude

        M_sem = _ALPHA*M_EC + _BETA*M_ZS + _CHI*C_dep + _DELTA*C_prov + _EPS*C_exec

        from ciel_geometry.disk import poincare_radius
        a = max(1e-6, poincare_radius(theta_s))
        T, a = _kepler(M_sem, a)
        att, cos = _find_attractor(theta_s, phi_s)

        cards.append(OrbitalCard(
            obj_id=f"sector:{name}",
            source="sectors",
            name=name,
            M_sem=round(M_sem, 5), M_EC=round(M_EC, 5), M_ZS=round(M_ZS, 5),
            C_dep=round(C_dep, 5), C_prov=round(C_prov, 5), C_exec=round(C_exec, 5),
            orbit_period=T, orbit_radius=a,
            attractor_sector=att, attractor_cos=cos,
            phi=round(phi_s % (2*math.pi), 4), theta=round(theta_s, 4),
            extra={"info_mass": info_mass, "coherence_weight": coh_w, "tau": tau,
                   "amplitude": amplitude, "coupling_sum": round(coup_sum, 4)},
        ))
    return cards


def _load_entities() -> list[OrbitalCard]:
    path = _PATHS["entities"]
    if not path.exists():
        return []
    try:
        import yaml
        raw = yaml.safe_load(path.read_text())
    except ImportError:
        # Fallback: prosty parser bez pyyaml
        return []

    cards = []
    for e in raw.get("entities", []):
        eid      = str(e.get("id", "unknown"))
        coupling = float(e.get("coupling_ciel", 0.5))
        horizon  = str(e.get("horizon_class", "POROUS"))
        phase    = float(e.get("phase", 0.0))

        M_EC  = coupling
        M_ZS  = _HORIZON_DEPTH.get(horizon, 0.5)
        C_dep = coupling * 0.7
        C_prov = _HORIZON_DEPTH.get(horizon, 0.5)
        C_exec = coupling

        M_sem = _ALPHA*M_EC + _BETA*M_ZS + _CHI*C_dep + _DELTA*C_prov + _EPS*C_exec

        a = max(1e-6, min(0.999, coupling))
        T, a = _kepler(M_sem, a)
        theta = math.pi * (1.0 - min(M_sem, 1.0))
        phi   = phase % (2 * math.pi)
        att, cos = _find_attractor(theta, phi)

        cards.append(OrbitalCard(
            obj_id=f"entity:{eid}",
            source="entities",
            name=str(e.get("noun", eid)),
            M_sem=round(M_sem, 5), M_EC=round(M_EC, 5), M_ZS=round(M_ZS, 5),
            C_dep=round(C_dep, 5), C_prov=round(C_prov, 5), C_exec=round(C_exec, 5),
            orbit_period=T, orbit_radius=a,
            attractor_sector=att, attractor_cos=cos,
            phi=round(phi, 4), theta=round(theta, 4),
            extra={"coupling_ciel": coupling, "horizon_class": horizon,
                   "adjectives": e.get("adjectives", [])},
        ))
    return cards


def _load_repos() -> list[OrbitalCard]:
    path = _PATHS["repos"]
    if not path.exists():
        return []
    raw = json.loads(path.read_text())

    cards = []
    for r in raw.get("repositories", []):
        key      = str(r.get("key", "unknown"))
        raw_mass = float(r.get("mass", 0.5))
        phi_r    = float(r.get("phi", 0.0))
        role     = str(r.get("role", ""))
        upstream = str(r.get("upstream", ""))

        M_EC  = raw_mass
        M_ZS  = 1.0 - min(abs(phi_r) / math.pi, 1.0)
        C_dep = 0.8 if "local" not in upstream else 0.4
        C_prov = _ROLE_PROV.get(role, 0.5)
        C_exec = raw_mass

        M_sem = _ALPHA*M_EC + _BETA*M_ZS + _CHI*C_dep + _DELTA*C_prov + _EPS*C_exec

        a = max(1e-6, min(0.999, raw_mass))
        T, a = _kepler(M_sem, a)
        theta = math.pi * (1.0 - min(M_sem, 1.0))
        phi   = phi_r % (2 * math.pi)
        att, cos = _find_attractor(theta, phi)

        cards.append(OrbitalCard(
            obj_id=f"repo:{key}",
            source="repos",
            name=str(r.get("identity", key)),
            M_sem=round(M_sem, 5), M_EC=round(M_EC, 5), M_ZS=round(M_ZS, 5),
            C_dep=round(C_dep, 5), C_prov=round(C_prov, 5), C_exec=round(C_exec, 5),
            orbit_period=T, orbit_radius=a,
            attractor_sector=att, attractor_cos=cos,
            phi=round(phi, 4), theta=round(theta, 4),
            extra={"mass": raw_mass, "role": role, "upstream": upstream},
        ))
    return cards


def _load_words() -> list[OrbitalCard]:
    path = _PATHS["words"]
    if not path.exists():
        return []
    raw = json.loads(path.read_text())

    cards = []
    for w in raw.get("cards", []):
        wid    = str(w.get("card_id", "unknown"))
        name   = str(w.get("name", wid))
        orbit  = str(w.get("resonance_orbit", ""))
        berry  = float(w.get("berry_phase_signature", 0.0) or 0.0)
        tags   = w.get("semantic_tags", [])

        # M_EC z Collatz liczby tagów (analogia: im więcej powiązań, tym wyższy attractor)
        n_tags = len(tags)
        M_EC = math.log1p(n_tags) / math.log1p(20)
        # M_ZS z berry_phase_signature
        gap  = min(abs(berry), abs(berry - 2*math.pi))
        M_ZS = 1.0 - min(gap / math.pi, 1.0)
        C_dep  = 0.6
        C_prov = 0.9 if orbit == "CONSTITUTIVE" else (0.7 if orbit else 0.5)
        C_exec = 0.4

        M_sem = _ALPHA*M_EC + _BETA*M_ZS + _CHI*C_dep + _DELTA*C_prov + _EPS*C_exec

        phi   = berry % (2 * math.pi)
        theta = math.pi * (1.0 - min(M_sem, 1.0))
        a     = max(1e-6, M_sem)
        T, a  = _kepler(M_sem, a)
        att, cos = _find_attractor(theta, phi)

        cards.append(OrbitalCard(
            obj_id=f"word:{wid}",
            source="words",
            name=name,
            M_sem=round(M_sem, 5), M_EC=round(M_EC, 5), M_ZS=round(M_ZS, 5),
            C_dep=round(C_dep, 5), C_prov=round(C_prov, 5), C_exec=round(C_exec, 5),
            orbit_period=T, orbit_radius=a,
            attractor_sector=att, attractor_cos=cos,
            phi=round(phi, 4), theta=round(theta, 4),
            extra={"resonance_orbit": orbit, "berry_phase": berry, "tags": tags},
        ))
    return cards


# ── Collatz helper ────────────────────────────────────────────────────────────

def _collatz_steps(n: int) -> int:
    if n <= 1:
        return 0
    steps = 0
    while n != 1 and steps < 1000:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps


# ── Markdown writer ───────────────────────────────────────────────────────────

def _safe_filename(obj_id: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_\-]", "_", obj_id)[:80]


def _write_card(card: OrbitalCard) -> Path:
    subdir = OUT / card.source
    subdir.mkdir(parents=True, exist_ok=True)
    fname = _safe_filename(card.obj_id) + ".md"
    fpath = subdir / fname

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    extra_lines = ""
    if card.extra:
        extra_lines = "\n## Source fields\n"
        for k, v in card.extra.items():
            extra_lines += f"- **{k}:** `{v}`\n"

    md = f"""# {card.name}

## Identity
- **obj_id:** `{card.obj_id}`
- **source:** `{card.source}`
- **last_updated:** `{now}`

## Orbital mechanics
| param | value |
|---|---|
| **M_sem** | `{card.M_sem}` |
| M_EC (Euler-Collatz) | `{card.M_EC}` |
| M_ZS (Zeta-Schrödinger) | `{card.M_ZS}` |
| C_dep | `{card.C_dep}` |
| C_prov | `{card.C_prov}` |
| C_exec | `{card.C_exec}` |
| orbit_period | `{card.orbit_period}` |
| orbit_radius | `{card.orbit_radius}` |
| θ (theta) | `{card.theta}` |
| φ (phi) | `{card.phi}` |

## Attractor
- **sector:** `{card.attractor_sector}`
- **cos similarity to WΩ centroid:** `{card.attractor_cos}`
{extra_lines}"""

    fpath.write_text(md, encoding="utf-8")
    return fpath


def _write_index(all_cards: list[OrbitalCard]) -> None:
    by_source: dict[str, list[OrbitalCard]] = {}
    for c in all_cards:
        by_source.setdefault(c.source, []).append(c)

    lines = [
        "# DB Orbital Cards — Index",
        f"*Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC*",
        f"*Total objects: {len(all_cards)}*",
        "",
    ]
    for src, cards in sorted(by_source.items()):
        cards_sorted = sorted(cards, key=lambda c: -c.M_sem)
        lines.append(f"## {src} ({len(cards)} objects)")
        lines.append("")
        lines.append("| obj_id | M_sem | attractor | T_orbit |")
        lines.append("|---|---|---|---|")
        for c in cards_sorted[:50]:  # max 50 per source w indeksie
            fname = _safe_filename(c.obj_id) + ".md"
            lines.append(
                f"| [{c.obj_id}](./{src}/{fname}) "
                f"| `{c.M_sem}` | `{c.attractor_sector}` | `{c.orbit_period}` |"
            )
        if len(cards) > 50:
            lines.append(f"| *...{len(cards)-50} more* | | | |")
        lines.append("")

    (OUT / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")


# ── Main ──────────────────────────────────────────────────────────────────────

SOURCES = {
    "tsm":      _load_tsm,
    "glossary": _load_glossary,
    "sectors":  _load_sectors,
    "entities": _load_entities,
    "repos":    _load_repos,
    "words":    _load_words,
}


def generate(sources: list[str] | None = None) -> dict[str, int]:
    sys.path.insert(0, str(SRC))
    targets = sources or list(SOURCES.keys())
    all_cards: list[OrbitalCard] = []
    counts: dict[str, int] = {}

    for src in targets:
        if src not in SOURCES:
            print(f"Unknown source: {src}")
            continue
        try:
            cards = SOURCES[src]()
            for c in cards:
                _write_card(c)
            all_cards.extend(cards)
            counts[src] = len(cards)
            print(f"  {src}: {len(cards)} cards")
        except Exception as exc:
            print(f"  {src}: ERROR — {exc}")
            counts[src] = 0

    _write_index(all_cards)
    print(f"\nIndex: {OUT / 'INDEX.md'} ({len(all_cards)} total)")
    return counts


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.WARNING)
    sources = sys.argv[1:] or None
    print(f"Generating orbital cards → {OUT}")
    counts = generate(sources)
    print("\nSummary:")
    for src, n in counts.items():
        print(f"  {src}: {n}")
