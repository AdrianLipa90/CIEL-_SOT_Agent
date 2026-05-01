# htri_local.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/htri/htri_local.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/htri/htri_local.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** OscillatorBank, CPUHtri, GPUHtri, LocalHTRI
- **functions:** plo_frequencies, _read_ram_available_gb, _read_disk_throughput_mb, __post_init__, step, run, __init__, run, __init__, run, _run_cuda, __init__, run, _sample

## Docstring
HTRI Local — Skalowanie Harmonic Topological Resonance Inducement
na sprzęt: i7-8750H (12 threads), GTX 1050 Ti (768 cores), 7.5 GB RAM.

H200 (14,080 blocks) → local hardware:
  CPU:  12 PLO (i7-8750H logical threads)
  GPU:  768 PLO (GTX 1050 Ti CUDA cores)
  RAM:  phase field volume
  Disk: M2/M3
