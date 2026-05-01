# recode_tsm_phases.py — scripts/recode_tsm_phases.py

## Identity
- **path:** `scripts/recode_tsm_phases.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _load_direct, main

## Docstring
Recode TSM phi_berry from SHA-256 hash to semantic encoder phases.

Run after ciel_encoder.py and sentence-transformers are installed.
Updates phi_berry metadata only — D_sense and D_context are never touched.

Usage:
    python3 scripts/recode_tsm_phases.py [--dry-run]
