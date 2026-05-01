# routes.py — src/ciel_sot_agent/gui/routes.py

## Identity
- **path:** `src/ciel_sot_agent/gui/routes.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _broadcast_sse, _scan_local_models, _find_gguf, _orbital_mode, _compute_groove_metrics, _load_wave_memory, _load_memory_stats, _load_repo_tensions, _load_pipeline_report, _is_small_model, _build_compact_prompt, _anchor_dialogue, _build_identity_preamble, _build_geometry_prompt, _parse_think_speak, _save_to_wave_archive, _handle_ciel_engine_message, _get_or_init_backend, _root, _load_orbital_bridge_report

## Docstring
Flask route handlers for the CIEL Quiet Orbital Control GUI.

Routes
------
GET  /               — Main dashboard (HTML)
GET  /api/status     — System status JSON (top status bar data)
GET  /api/panel      — Full panel state JSON
GET  /api/models     — Installed GGUF models JSON
POST /api/models/ens
