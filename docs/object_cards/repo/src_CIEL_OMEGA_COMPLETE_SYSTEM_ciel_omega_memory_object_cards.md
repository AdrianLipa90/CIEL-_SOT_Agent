# object_cards.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/object_cards.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/object_cards.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** ObjectCard, FeatureCard, ClosureOp, AffectCard, SentenceEquation
- **functions:** _pos_tag, _extract_concepts, _extract_features, _extract_closureops, _cyclic_dist, _circular_mean_std, _semantic_mass, build_cards, build_features, build_closure_ops, affect_of, get_affects, parse_sentence, get_cards, get_features, related, opposites, phase_neighbors, attractors, adaptive_delta

## Docstring
CIEL Object Cards — Keplerian semantic ontology.

Grammar-as-physics: parts of speech are dynamical roles in phase space.

  ┌─ ObjectCard (noun) ──────────────────────────────────────────────────────┐
  │  M(c) = freq × closure_mean × log1p(winding_mean) × phase_stability     │
  │  Asymmetric W_ij
