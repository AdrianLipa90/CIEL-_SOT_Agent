# ciel_orchestrator.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/ciel_orchestrator.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/ciel_orchestrator.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** CIELOrchestrator
- **functions:** build_arg_parser, load_config, main, __init__, boot, shutdown, ping, status_snapshot, process, _print_result, interactive_session

## Docstring
CIEL/Ω — Canonical main orchestrator.

Hierarchy:
  CielEngine        -> core facade for step/interact
  CIELOrchestrator  -> human-facing system orchestrator
  main.py           -> canonical root entrypoint for local tests
  ciel_client.py    -> minimal communication client (next layer)
