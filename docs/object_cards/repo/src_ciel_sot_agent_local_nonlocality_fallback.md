# local_nonlocality_fallback.py — src/ciel_sot_agent/local_nonlocality_fallback.py

## Identity
- **path:** `src/ciel_sot_agent/local_nonlocality_fallback.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _read_cpu_percent, _read_mem_percent, _read_load_avg, _read_process_count, _read_disk_bytes, _read_net_bytes, _time_of_day_phase, read_pc_phases, _run_eba_with_hidden, _aggregate_eba, run_local_nonlocality_fallback, merge_with_canonical, save_report, load_last_report, main, _sample, _n

## Docstring
Local Nonlocality Fallback — PC state as hidden-channel phase source.

When the canonical HolonomicMemoryOrchestrator produces low nonlocal_coherent_fraction
(< 0.40), this module derives 8 hidden-state phases from live PC metrics and re-runs
EBA loop evaluation with these richer hidden states.

PC 
