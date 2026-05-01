# ciel_orbital_monitor.py — scripts/ciel_orbital_monitor.py

## Identity
- **path:** `scripts/ciel_orbital_monitor.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** ResourceOscillator, OrbitalResourceSystem
- **functions:** main, update_from_value, kuramoto_force, current_value, order_param_contribution, __init__, _init_oscillators, _osc, collect, step, _compute_metrics, format_dashboard

## Docstring
CIEL Orbital Resource Monitor

Każdy zasób systemowy = oscylator z fazą.
Kuramoto coupling synchronizuje zasoby.
Orbity 0-4 jak w Relational_Potential_Physics.

Zasoby → Orbity:
  Orbit 0 (core):        CPU rdzenie
  Orbit 1 (runtime):     GPU, RAM
  Orbit 2 (registry):    Cache, Swap
  Orbit 3 (int
