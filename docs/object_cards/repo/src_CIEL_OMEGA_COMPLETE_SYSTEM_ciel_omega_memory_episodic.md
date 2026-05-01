# episodic.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/episodic.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/episodic.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** Episode, EpisodicMemory
- **functions:** to_dict, __init__, compute_input_force, store, retrieve, _context_matches, _should_consolidate, compute_consolidation_score, get_consolidation_candidates, mark_consolidated, _save_to_disk, _load_from_disk, get_statistics

## Docstring
CIEL/Ω Memory Architecture - M2: Episodic Memory

Memory of events and sequences. Records what happened, when, in what context,
and with what result. Medium timescale, good temporal localization.

τ=12, r=0.55, g=0.45, δ_max=0.16π

Copyright (c) 2025 Adrian Lipa / Intention Lab
Licensed under the CI
