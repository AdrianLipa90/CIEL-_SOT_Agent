# orbital_bridge.py — src/ciel_sot_agent/orbital_bridge.py

## Identity
- **path:** `src/ciel_sot_agent/orbital_bridge.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _load_json_if_exists, _build_sync_manifest, _build_runtime_gating, _bridge_markdown, build_orbital_bridge, main

## Docstring
Orbital bridge — runs the global orbital coherence pass and writes
bridge state, health, and control-recommendation manifests.

Connects the CIEL integration kernel to the Orbital diagnostic subsystem
living under ``integration/Orbital/``, ensuring phase-coherence and
resource health are reported at
