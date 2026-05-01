# htri_scheduler.py — src/ciel_sot_agent/htri_scheduler.py

## Identity
- **path:** `src/ciel_sot_agent/htri_scheduler.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _kuramoto_step, run, get_state, get_optimal_threads

## Docstring
HTRI Scheduler — Kuramoto na 12 wątkach CPU (i7-8750H).

Skalowanie H200 → local:
  H200:  14 080 bloków, spread 28 Hz → bicie 7.83 Hz
  Local: 12 wątków (logical cores), ta sama topologia Kuramoto, ta sama zasada.

Eksportuje: coherence r → n_threads_optimal dla llama.cpp.
Zapis do ~/Pulpit/CIEL_me
