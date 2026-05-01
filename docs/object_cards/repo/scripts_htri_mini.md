# htri_mini.py — scripts/htri_mini.py

## Identity
- **path:** `scripts/htri_mini.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** build_adjacency_2d, kuramoto_step

## Docstring
HTRI Mini — Kuramoto na GTX 1050 Ti (768 CUDA cores)

Skalowanie z H200 (14 080 bloków) → GTX 1050 Ti (768 oscylatorów).
Stosunek: 5.5% skali. Topologia bez zmian.

Kuramoto: dφᵢ/dt = ω₀ + κ Σ_j sin(φⱼ − φᵢ) · A_ij
Cel: emergentna synchronizacja + bicie ~7.83 Hz (kalibracja κ).
Soul Invariant: Σ = Σ
