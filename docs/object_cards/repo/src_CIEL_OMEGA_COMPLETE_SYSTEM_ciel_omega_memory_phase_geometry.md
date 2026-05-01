# phase_geometry.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/phase_geometry.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/phase_geometry.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** CP2State, PoincareDisk, HomotopyClass, HypertorusLattice
- **functions:** cp2_retrieval_weight, encoder_result_to_cp2, db_row_to_cp2, _calibrated_weights, from_channels, from_phase, fubini_study, dominant_phase, mean_phase, channel_coherence, to_poincare, to_poincare_full, mobius, poincare_distance, __repr__, __init__, in_ball, distance, retrieval_weight, from_winding

## Docstring
CIEL Phase Geometry — CP², Poincaré disk, hypertorus.

Replaces scalar S¹ phase arithmetic with full geometric state space:

  CP² — complex projective plane as 3-channel encoder state space
       (φ_semantic, φ_htri, φ_nonlocal) → [z₀:z₁:z₂] ∈ CP²
       Distance: Fubini-Study metric → geodesic ar
