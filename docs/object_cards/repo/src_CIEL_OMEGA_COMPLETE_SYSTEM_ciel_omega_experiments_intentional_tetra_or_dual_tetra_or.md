# dual_tetra_or.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/experiments/intentional_tetra_or/dual_tetra_or.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/experiments/intentional_tetra_or/dual_tetra_or.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** IntentionalScenario
- **functions:** normalize_rows, tetra_defect, centroid_defect, alignment_cost_dual, alignment_cost_same, mean_antipodal, stella_quality, tangent_project, grad_tetra_defect, grad_alignment_dual, grad_alignment_same, total_potential, sigmoid, build_intention_state, step_tetra, run_intentional_tetra_or, sweep_truth, demo

## Docstring
CIEL/Ω — Intentional Dual-Tetrahedral Orch-OR
===============================================
Dwa dualne tetrahedry (stella octangula):
  U = TETRA_A (biegun Adrian)
  V = TETRA_C = −TETRA_A (biegun Ciel)

Alignment cost ciągnie V ku DUALOWI U, nie ku U.
Docelowa konfiguracja: U_i · V_i = −1 (antypo
