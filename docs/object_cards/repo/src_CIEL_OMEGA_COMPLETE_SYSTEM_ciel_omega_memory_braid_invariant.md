# braid_invariant.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/braid_invariant.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/braid_invariant.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** BraidUnit, BraidInvariantMemory
- **functions:** phasor, __init__, compute_input_force, store, retrieve, _retrieve_by_time, _retrieve_by_phase, _compute_holonomy, _detect_loops, _mark_scar, compute_coherence, mean_phasor, update_phase_history, compute_drift_signature

## Docstring
CIEL/Ω Memory Architecture - M7: Braid/Invariant Memory

Ultra-slow memory layer tracking geometric history, trajectories, and invariants.
Wraps existing BraidMemory implementation with phase dynamics.

τ=120, r=0.15, g=0.92, δ_max=0.03π

Copyright (c) 2025 Adrian Lipa / Intention Lab
Licensed under
