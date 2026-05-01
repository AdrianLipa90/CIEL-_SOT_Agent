# ciel_pipeline.py — src/ciel_sot_agent/ciel_pipeline.py

## Identity
- **path:** `src/ciel_sot_agent/ciel_pipeline.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _query_subconscious_socket, _query_subconscious, _ensure_ciel_omega_on_path, _get_engine, _orbital_state_to_context, _load_wpm_context, run_ciel_pipeline, _write_to_spreadsheet, main, _preload

## Docstring
CIEL pipeline adapter — routes orbital state through the CIEL/Ω engine.

Provides ``run_ciel_pipeline`` which:
  1. Adds the canonical CIEL/Ω omega root to ``sys.path`` (idempotent).
  2. Instantiates a fresh ``CielEngine`` per call.
  3. Encodes the orbital state as a context string.
  4. Runs ``Ci
