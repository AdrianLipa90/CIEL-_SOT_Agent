# ciel_encoder.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/ciel_encoder.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/ciel_encoder.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** EncoderResult, CIELEncoder
- **functions:** _get_channel_weights, _hash_embedding, _hash_phase, _load_texts_from_jsonl, get_encoder, __post_init__, __init__, encode, retrain_from_corpus, _embed, _embed_batch, _get_model, _phase_projection, _blend_htri, _blend_nonlocal, _get_nonlocal_phase, _get_htri_phase, _sector_distribution, _local_coherence, _update_context

## Docstring
CIEL Semantic Phase Encoder.

Replaces SHA-256 hash phase with a real semantic embedding projected onto S¹.
Architecture: sentence-transformer → PCA phase projection → sector softmax.

Outputs per text:
    phase   float  [0, 2π)  — semantic position on circle
    sector  ndarray(10,)    — soft assi
