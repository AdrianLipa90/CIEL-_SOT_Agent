# phase_equation_of_motion.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/phase_equation_of_motion.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/phase_equation_of_motion.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** PhaseInfoSystem
- **functions:** delta_H, R_H, dR_H_dgamma, V_information, dV_I_dgamma, V_deformation, V_total, dV_total_dgamma, white_thread_current, white_thread_zeta_weighted, make_zeta_wt_fn, collatz_sequence, collatz_rhythm, collatz_forcing, acceleration, wrap_angle, heisenberg_load, fermion_lock_score, phase_sector, euler_constraint_violation

## Docstring
CIEL/Ω — Równanie Ruchu Informacji Fazowej
============================================
Konkretna derywacja. Każdy człon ma pochodzenie.

Obiekt fundamentalny:
    I_k = σ_k · exp(i·γ_k)        informacja zespolona (skalar)

Równanie ruchu (dla faz γ_k):
    μ_k · γ̈_k = −∂V_rel/∂γ_k     siła holono
