# bootstrap_runtime.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/bootstrap_runtime.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/bootstrap_runtime.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** candidate_paths, ensure_runtime_paths

## Docstring
Shared runtime bootstrap for local CIEL/Ω entry surfaces.

This module centralizes path normalization so orchestrator/client/unified do not
carry divergent bootstrap logic. It supports both package-style execution and
local script execution from the Omega root.
