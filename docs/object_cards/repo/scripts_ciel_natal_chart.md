# ciel_natal_chart.py — scripts/ciel_natal_chart.py

## Identity
- **path:** `scripts/ciel_natal_chart.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** PlanetPos, Aspect
- **functions:** _ephem_planet, compute_positions, find_aspects, _planet_xy, render_chart, main, draw_wheel

## Docstring
ciel_natal_chart.py — Horoskop natalny zintegrowany z fazami Berry CIEL.

Planety jako operatory na przestrzeni fazowej:
  φ_planet = ekliptyczna długość planety / (2π) → faza Berry
  Aspekty   = W_ij między planetami (cosine similarity faz)
  Domy      = 12 sektorów kołowych, każdy z φ_domain

Usag
