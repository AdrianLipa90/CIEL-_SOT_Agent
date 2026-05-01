# ciel_benchmark.py — scripts/ciel_benchmark.py

## Identity
- **path:** `scripts/ciel_benchmark.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** measure_cpu_during, quality_score, benchmark_model, print_summary, _poll, _infer

## Docstring
CIEL Benchmark — pomiar energii i jakości modeli GGUF

Metryki:
  - Czas generacji (s)
  - Tokeny/sekundę
  - CPU% podczas generacji (proxy energii)
  - Energia = czas × avg_cpu% (arbitrarne jednostki)
  - Jakość: długość sensownej odpowiedzi, brak powtórzeń, spójność

Użycie:
  python scripts/ciel_
