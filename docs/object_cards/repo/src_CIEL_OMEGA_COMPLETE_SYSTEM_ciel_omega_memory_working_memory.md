# working_memory.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/working_memory.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/working_memory.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** WorkingMemory
- **functions:** __init__, normalize_text, _compute_identity_alignment, _episode_id, compute_input_force, store, observe, decay, reinforce, retrieve, active_items, snapshot, retrieve_raw, evict_decayed

## Docstring
CIEL/Ω Memory Architecture - M1 Working Memory

Conservative active operational field between perception and consolidation.
Working memory is short-lived, decays without reinforcement, and does not
write directly to IdentityField or M6.
