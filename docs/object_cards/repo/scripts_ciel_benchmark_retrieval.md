# ciel_benchmark_retrieval.py — scripts/ciel_benchmark_retrieval.py

## Identity
- **path:** `scripts/ciel_benchmark_retrieval.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _load, _keywords_from_tags, _text_relevant, _build_query_set, _cyclic_dist, _cosine, _rank_ciel_full, _rank_phase_only, _rank_cosine, _rank_random, _precision_at_k, _reciprocal_rank, _phase_resonance, _mean_closure, _run_benchmark, main

## Docstring
CIEL Retrieval Benchmark — 4 warianty, tylko wewnętrzny pipeline.

Porównuje:
  CIEL-FULL       — holonomic_weight (faza + CP² + Poincaré + Hebbian spreading)
  CIEL-PHASE-ONLY — ranking po odległości fazowej |φ_berry − φ_query|
  CIEL-COSINE     — cosine similarity embeddingów (odpowiednik vector D
