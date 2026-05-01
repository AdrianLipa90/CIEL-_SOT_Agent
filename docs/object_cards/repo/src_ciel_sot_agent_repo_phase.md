# repo_phase.py — src/ciel_sot_agent/repo_phase.py

## Identity
- **path:** `src/ciel_sot_agent/repo_phase.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** RepositoryState
- **functions:** load_registry, load_couplings, weighted_euler_vector, closure_defect, pairwise_tension, all_pairwise_tensions, build_sync_report

## Docstring
Repository phase state and synchronisation report builder.

Models each repository as a phase-carrying identity with a complex spin,
mass, and role.  Exposes ``build_sync_report`` which loads the repository
registry and coupling map, computes the weighted Euler vector and closure
defect, and returns
