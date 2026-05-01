# affective_lexicon.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/affective_lexicon.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/affective_lexicon.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** LexiconEntry, AffectiveLexicon, _PatchedLex
- **functions:** _vad_to_phase, _vad_distance, _cyclic_distance, get_lexicon, annotate, phi_affective, memorise_id, as_tsm_row, __init__, _rebuild_index, add, get, query_text, query_vad, query_resonant, annotate_text, stats, import_to_holonomic, import_to_holonomic

## Docstring
CIEL Affective-Semantic Lexicon — VAD model with holonomic phase geometry.

Three-dimensional affect space:
    V  — Valence     [-1, +1]  (negative ↔ positive)
    A  — Arousal     [ 0,  1]  (calm ↔ excited)
    D  — Dominance   [-1, +1]  (submissive ↔ dominant)

Phase encoding:
    phi_V = 2π * (V
