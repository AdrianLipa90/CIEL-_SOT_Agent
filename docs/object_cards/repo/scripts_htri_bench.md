# htri_bench.py — scripts/htri_bench.py

## Identity
- **path:** `scripts/htri_bench.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _post, _reset, run_round, stats, main

## Docstring
HTRI Benchmark — porównanie inference z n_threads=4 (baseline) vs HTRI-optimal.

Metodologia:
  Runda A: POST /api/chat/message, n_threads=4 (hardcoded baseline)
  Runda B: POST /api/chat/message, n_threads=htri_optimal (z Kuramoto)

Mierzy: czas odpowiedzi (ms), długość odpowiedzi (chars), chars/ms
