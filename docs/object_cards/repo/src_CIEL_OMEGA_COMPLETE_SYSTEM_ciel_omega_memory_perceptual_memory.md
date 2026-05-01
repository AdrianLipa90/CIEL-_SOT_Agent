# perceptual_memory.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/perceptual_memory.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/perceptual_memory.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** PerceptualMemory
- **functions:** __init__, normalize_text, _compute_identity_alignment, _infer_novelty, _source_id, compute_input_force, store, observe, decay, retrieve, active_items, snapshot, evict_decayed

## Docstring
CIEL/Ω Memory Architecture - M0 Perceptual Memory

Conservative perceptual ingress buffer. M0 is a fast first-order channel with
strong decay, high plasticity, and no direct write path into IdentityField or M6.
It stores raw percepts transiently and supports salience-ranked retrieval.
