# semantic_memory.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/semantic_memory.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/semantic_memory.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** SemanticMemory
- **functions:** __init__, _normalize_text, _stem, _extract_concept_key, _parse_semantics, _wrap, _episode_id, _compute_identity_alignment, _similarity, _existing_contradiction_penalty, _compute_novelty, semantic_distance, observe_episode, _traces_for_key, compute_consolidation_score, check_semantic_candidate_creation, consolidate_candidate, retrieve, get_statistics, snapshot

## Docstring
CIEL/Ω Memory Architecture - M3 Semantic Memory

Conservative semantic memory channel. Consolidates repeated meaning from M2,
blocks contradictions, and provides simple retrieval.
