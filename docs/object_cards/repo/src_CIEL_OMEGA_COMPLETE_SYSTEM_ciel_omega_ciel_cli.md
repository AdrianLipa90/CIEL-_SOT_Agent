# cli.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/ciel/cli.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/ciel/cli.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _run_client, _json_default, run_engine, smoke_test

## Docstring
Canonical CLI helpers routed through the Omega communication surface.

The CLI no longer bypasses the orchestrator by talking directly to the engine.
It uses the canonical local communication client for one-shot calls and smoke
probes.
