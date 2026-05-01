# phased_state.py — src/ciel_sot_agent/phased_state.py

## Identity
- **path:** `src/ciel_sot_agent/phased_state.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** FileState
- **functions:** sha256_seed, frac64, f_size, _require_finite_real, _require_hash_fraction, _require_connection_count, _require_non_negative_count, _require_positive_weight, f_conn, f_anchor, f_flow, weight_type, weight_layer, relational_relevance, compute_raw_energy, normalize, compute_phase, build_states

## Docstring
Phased-state model for repository and file-level identity scoring.

Computes a deterministic identity phase for each file/node from its
hash-derived fraction and computes selection energy from explicit
relational metadata such as size, type, layer, connectivity, anchors,
and upstream/downstream stru
