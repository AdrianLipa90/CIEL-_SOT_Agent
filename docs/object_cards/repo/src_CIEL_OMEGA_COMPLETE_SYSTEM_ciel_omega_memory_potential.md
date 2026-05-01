# potential.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/potential.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/potential.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** MemoryPotential
- **functions:** __init__, compute_alignment_potential, compute_conflict_potential, compute_drift_potential, compute_noise_potential, compute_eba_potential, compute_static_potential, compute_dissipation_functional, compute_monitored_energy, compute_force_from_potential, compute_global_memory_defect, compute_global_identity_defect, analyze_stability

## Docstring
CIEL/Ω Memory Architecture - Memory Potentials

Defines potential energy landscape that governs memory dynamics.
Memories evolve to minimize total potential: alignment with identity,
conflict between channels, drift from anchors, and noise.

V_mem = V_align + V_conflict + V_drift + V_noise

Copyrigh
