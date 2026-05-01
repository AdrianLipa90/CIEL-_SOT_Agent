# generate_orbital_cards.py — scripts/generate_orbital_cards.py

## Identity
- **path:** `scripts/generate_orbital_cards.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** OrbitalCard
- **functions:** _kepler, _bloch_vec, _find_attractor, _load_tsm, _load_glossary, _load_sectors, _load_entities, _load_repos, _load_words, _collatz_steps, _safe_filename, _write_card, _write_index, generate, __post_init__

## Docstring
Generator kart orbitalnych — każdy obiekt w każdej bazie dostaje kartę z M_sem.

Semantyczny Collatz + Zeta-Schrödinger = M_sem, nie hash, nie rozmiar pliku.
Każda karta zawiera:
  - M_sem, M_EC, M_ZS, C_dep, C_prov, C_exec
  - orbit_period, orbit_radius
  - attractor_sector — który z 10 centroidów 
