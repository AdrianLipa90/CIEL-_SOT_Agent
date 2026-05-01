# _registry.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/_registry.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/_registry.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** get_module, get_encoder, get_holonomic, get_calibration, get_semantic_scorer

## Docstring
Module singleton registry — load once, return cached.

Replaces scattered spec_from_file_location calls across the codebase.
Every module loaded through here is guaranteed to exist exactly once in
sys.modules under a stable name, regardless of how many callers request it.

Usage:
    from ciel_omega
