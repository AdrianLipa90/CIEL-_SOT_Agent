# serve_portal.py — scripts/serve_portal.py

## Identity
- **path:** `scripts/serve_portal.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** CIELHandler
- **functions:** read_live_state, read_orbital_data, read_geometry_data, read_sessions, read_memories, run_pipeline_step, _mime, _watch_and_rebuild, main, log_message, do_GET, do_POST

## Docstring
CIEL Portal Server — serwuje ~/.claude/ciel_site/ przez HTTP.

Funkcje:
  - Serwuje portal jako http://localhost:7481/
  - /api/live  — live metryki z pickle (cycle, health, ethical, closure, emotion)
  - /api/state — pełny stan orbitalny z ostatniego raportu
  - Wstrzykuje do każdej strony HTML aut
