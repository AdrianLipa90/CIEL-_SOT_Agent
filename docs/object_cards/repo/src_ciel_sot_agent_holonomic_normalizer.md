# holonomic_normalizer.py — src/ciel_sot_agent/holonomic_normalizer.py

## Identity
- **path:** `src/ciel_sot_agent/holonomic_normalizer.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** HolonomicCallbacks
- **functions:** wrap, circular_barycenter, circular_distance, symmetrize_couplings, clip_couplings, renormalize_couplings, _get, _set, _sector, _select_control_mode, holonomic_system_normalizer_v2

## Docstring
Holonomic phase normalizer for the CIEL integration kernel.

Provides circular-arithmetic utilities (phase wrapping, circular barycenter,
circular distance) and the HolonomicNormalizer class that applies weighted
renormalization across a map of named phase-carrying nodes.
