# synchronize_v2.py — src/ciel_sot_agent/synchronize_v2.py

## Identity
- **path:** `src/ciel_sot_agent/synchronize_v2.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** resolve_sync_paths, build_sync_report_v2, main

## Docstring
Synchronise entry point (v2) — extended sync with v2 schema support.

Extends the v1 synchronizer with enriched coupling weights, pairwise
tension vectors, and structured JSON report output written to the
``integration/reports/`` directory.  Invoked via ``ciel-sot-sync-v2``.
