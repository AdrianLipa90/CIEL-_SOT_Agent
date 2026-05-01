# optimize_wij.py — scripts/optimize_wij.py

## Identity
- **path:** `scripts/optimize_wij.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _build_system, _coupling_pairs, _vec_to_couplings, _run_steps, make_objective, main, _ci_full, objective

## Docstring
W_ij coupling optimizer for the CIEL orbital system.

Minimizes closure_penalty over the scalar coupling matrix W_ij in
integration/Orbital/main/manifests/couplings_global.json using
scipy L-BFGS-B with bounds W_ij ∈ [0.01, 1.0].

Objective:
    closure_penalty = Σ_i |Σ_j A_ij(W) * τ_j - e^{iφ_i}|² 
