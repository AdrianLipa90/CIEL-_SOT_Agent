# semantic_scorer.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/semantic_scorer.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/semantic_scorer.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** _Card, _NonlocalLink, _NOEMAObs
- **functions:** _extract, _score_card, _observe, _build_links, score_with_noema, build_nonlocal_index

## Docstring
CIEL Semantic Scorer — MemoryScorer + NOEMAObserver + SemanticExtractor + NonlocalGraphBuilder.

Inline port from ciel_algo_repo (no hard dependency on external path).
Provides semantic scoring, NOEMA observation metrics, and nonlocal graph construction
for CIEL holonomic memory entries.

Public API
