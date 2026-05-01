# orbital_memory_loop.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/ciel/orbital_memory_loop.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/ciel/orbital_memory_loop.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** RuntimeOrbitalSignals, OrbitalLoopConfig, OrbitalLoopResult
- **functions:** _clamp, derive_runtime_orbital_params, run_orbital_loop, _coherence_flags, build_memory_meta, build_wave_attrs, build_runtime_policy, to_dict

## Docstring
Bridge orbital diagnostics into runtime and durable memory.

This module turns the previously detached orbital subsystem into a runtime loop:

input -> orbital snapshot -> control recommendation -> memory capture/promotion

The bridge is intentionally conservative:
- orbital failures never crash the
