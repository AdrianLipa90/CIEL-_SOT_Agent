# identity_memory.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/identity_memory.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/identity_memory.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** IdentityMemory
- **functions:** __init__, observe_identity_field, compute_consolidation_score, check_anchor_candidate_creation, take_snapshot, get_mature_candidates, _compute_trace_confidence, get_statistics, __repr__, store, retrieve, compute_input_force

## Docstring
CIEL/Ω Memory Architecture - M6 Identity Memory Channel

M6 stores historical traces of identity stabilization. It is NOT a duplicate
of IdentityField - rather, it records the slow evolution of identity over time.

Key principles:
- IdentityField remains the attractor and operator
- M6 records histo
