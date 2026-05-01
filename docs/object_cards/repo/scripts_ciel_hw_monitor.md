# ciel_hw_monitor.py — scripts/ciel_hw_monitor.py

## Identity
- **path:** `scripts/ciel_hw_monitor.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _read_cpu, _read_ram, _read_gpu, _read_top_procs, _assess, _render, heisenberg_clip, snapshot, main

## Docstring
CIEL Hardware Monitor — CPU / RAM / GPU / VRAM / SWAP.

Mierzy zasoby sprzętowe i raportuje w kontekście CIEL:
- Czy HTRI może bezpiecznie uruchomić GPU steps?
- Czy swap jest pod presją (OOM risk)?
- Jaka jest faktyczna przepustowość obliczeniowa?

Usage:
    python3 scripts/ciel_hw_monitor.py     
