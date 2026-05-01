# holonomic_memory.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/holonomic_memory.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/holonomic_memory.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** HolonomicMemory
- **functions:** _cyclic_distance, _holonomic_weight, stamp_pipeline_output, import_ciel_memories, __init__, _ensure_nonlocal_index, _connect, _ensure_schema, update_holonomy, stamp_new, _get_hebbian_params, hebbian_update, edge_neighbors, edge_stats, retrieve_resonant, retrieve_weighted, stats, _text_phase, _text_w_semantic, _blend_phase

## Docstring
Holonomic Semantic Memory — phase-weighted retrieval layer over TSM.

Extends TSMWriterSQL with Berry holonomy columns. Each memory entry
accumulates a geometric phase as it passes through orbital cycles.
Retrieval is phase-resonant: entries whose phi_berry is close (cyclically)
to the current orbit
