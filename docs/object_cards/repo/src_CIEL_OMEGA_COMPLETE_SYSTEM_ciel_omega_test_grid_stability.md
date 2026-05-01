# test_grid_stability.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/test_grid_stability.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/test_grid_stability.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** run_stability_test, test_problematic_case

## Docstring
CIEL/Ω Memory Architecture - Grid Stability Test

Regression test for numerical stability across parameter grid:
- Seeds: 0-49
- Timesteps: {0.05, 0.1, 0.2, 0.3}
- Initial scales: {0.5, 1.0}

Tests whether V_static, D_mem, and D_id decrease under zero forcing.

Copyright (c) 2025 Adrian Lipa / Inten
