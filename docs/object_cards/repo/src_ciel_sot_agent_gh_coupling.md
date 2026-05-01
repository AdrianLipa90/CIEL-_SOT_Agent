# gh_coupling.py — src/ciel_sot_agent/gh_coupling.py

## Identity
- **path:** `src/ciel_sot_agent/gh_coupling.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** build_live_coupling, main

## Docstring
GitHub coupling subsystem (v1) — live upstream-aware phase coupling.

Fetches current upstream HEAD SHAs for registered repositories, propagates
phase shifts through the coupling map, and emits a refreshed JSON coupling
report.  Invoked via the ``ciel-sot-gh-coupling`` console script.
