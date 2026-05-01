# synchronize.py — src/ciel_sot_agent/synchronize.py

## Identity
- **path:** `src/ciel_sot_agent/synchronize.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _apply_thermal_noise, main

## Docstring
Synchronise entry point (v1) — builds and emits a sync report to stdout.

Reads the repository registry and coupling map from the ``integration/``
directory, calls ``repo_phase.build_sync_report``, and prints the result
as formatted JSON.  Invoked via the ``ciel-sot-sync`` console script.
