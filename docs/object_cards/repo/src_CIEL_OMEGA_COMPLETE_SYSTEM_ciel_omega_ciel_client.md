# ciel_client.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/ciel_client.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/ciel_client.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** CIELClient
- **functions:** build_arg_parser, main, __init__, _system_prompt, shutdown, handshake, status, process, communicate, interactive_session

## Docstring
CIEL/Ω — minimal local communication client.

This client is intentionally small and deterministic for local tests.
Hierarchy:
  CielEngine        -> core facade
  CIELOrchestrator  -> top-level orchestration
  CIELClient        -> minimal local communication surface
  main()            -> local tes
