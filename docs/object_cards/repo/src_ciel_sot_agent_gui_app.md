# app.py — src/ciel_sot_agent/gui/app.py

## Identity
- **path:** `src/ciel_sot_agent/gui/app.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** create_app, main

## Docstring
Flask application factory and entry-point for the CIEL Quiet Orbital Control GUI.

The GUI is intentionally a *consumer* of prepared state — it reads manifests,
reports, and session files written by backend modules rather than performing
heavy computation itself.  This follows the "GUI consumes stat
