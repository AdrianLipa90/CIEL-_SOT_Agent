# procedural_memory.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/procedural_memory.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/procedural_memory.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** ProceduralMemory
- **functions:** __init__, _wrap, normalize_text, _extract_goal_action, _procedure_key, _episode_id, _compute_identity_alignment, _extract_success, _similarity, compute_input_force, observe_episode, _existing_contradiction_penalty, _traces_for_key, _goal_level_contradiction, compute_consolidation_score, check_candidate_creation, consolidate_candidate, retrieve, snapshot, retrieve_raw

## Docstring
CIEL/Ω Memory Architecture - M4 Procedural Memory

Conservative procedural memory channel. Consolidates reusable procedures from
repeated successful episodes for the same goal while blocking contradictions.
