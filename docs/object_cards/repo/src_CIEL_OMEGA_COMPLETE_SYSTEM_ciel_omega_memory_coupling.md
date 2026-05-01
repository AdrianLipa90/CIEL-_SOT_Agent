# coupling.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/coupling.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/coupling.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** CouplingEngine
- **functions:** print_coupling_summary, __init__, _validate_matrix, compute_coupling_force, compute_all_coupling_forces, get_strongest_couplings, analyze_coupling_hierarchy, compute_phase_shift_matrix, get_default_role_amplitudes

## Docstring
CIEL/Ω Memory Architecture - Coupling Matrix

Defines inter-channel coupling strengths J_kj that govern how memory
channels influence each other. Asymmetric by design: impact of relation
on identity differs from impact of identity on relation.

Copyright (c) 2025 Adrian Lipa / Intention Lab
Licensed
