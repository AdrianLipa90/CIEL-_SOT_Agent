# euler_constraint.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/constraints/euler_constraint.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/constraints/euler_constraint.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** EulerConstraintReport
- **functions:** _wrap, _circ_mean, _safe_angle_mean, _build_core_phase_vector, _canonical_id_to_phase, _priority_weight, _build_vocabulary_phase_vector, _build_affect_phase_vector, _memory_stats, _sector_metrics, _pairwise_tension, circular_target_phase, regulation_strength, evaluate_unified_euler_constraint, _apply_phase_pull, apply_active_euler_feedback, as_dict, euler_constraint_violation, phase_sector

## Docstring
Unified multi-sector Euler/EBA/semantic closure for CIEL/Ω.

This module now supports four phase sectors:
- memory
- core
- vocabulary / semantic
- affect

It also provides active feedback with rollback-safe helpers so the same
constraint can be used both as a metric and as a runtime regulator.
