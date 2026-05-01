# phase_sweep_analysis.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/phase_sweep_analysis.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/phase_sweep_analysis.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** run_scenario, sweep, pearson, correlations, show_sweep, show_corr, main, avg

## Docstring
CIEL/Ω — Phase Dynamics: Sweep, Correlations, Zeta-Weighted WT (v2)
=====================================================================
Poprawki vs v1:
  FIX A: zeta-weighted WT wstrzyknięty do dynamiki przez wt_fn callback
  FIX B: sigma_zeta sweep jest dynamiczny (sigma jest parametrem systemu)

