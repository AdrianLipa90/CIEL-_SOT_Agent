# ciel_launch.py — scripts/ciel_launch.py

## Identity
- **path:** `scripts/ciel_launch.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** ensure_gui_deps, start_pipeline, create_desktop_file, main, _open_browser

## Docstring
CIEL/Ω System Launcher

Uruchamia cały system CIEL:
  1. Sprawdza i instaluje zależności GUI
  2. Uruchamia CIEL pipeline (synchronize → orbital_bridge) w tle
  3. Otwiera GUI NiceGUI z ikoną Logo1.png w przeglądarce

Użycie:
    python scripts/ciel_launch.py
    python scripts/ciel_launch.py --no-p
