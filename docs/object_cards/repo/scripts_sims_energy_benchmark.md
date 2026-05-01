# energy_benchmark.py — scripts/sims/energy_benchmark.py

## Identity
- **path:** `scripts/sims/energy_benchmark.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** power_W, energy_mJ, read_proc_stat, measure, baseline, bench_m08, bench_pipeline, claude_api_estimate, main, run, run

## Docstring
CIEL Energy Benchmark — zużycie energii lokalnego pipeline vs Claude API (szacunek).

Mierzy:
  - M0-M8 per krok (hot, in-process)
  - Full pipeline (cold, subprocess)
  - Szacunek energii sesji 30 wiad.
  - Porównanie z kosztem energetycznym Claude API (server-side)

RAPL wymaga root (intel-rapl:0/
