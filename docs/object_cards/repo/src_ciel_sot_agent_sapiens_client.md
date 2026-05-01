# sapiens_client.py — src/ciel_sot_agent/sapiens_client.py

## Identity
- **path:** `src/ciel_sot_agent/sapiens_client.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** SapiensIdentity, SapiensTurn, SapiensSession
- **functions:** _now, _state_geometry, _surface_policy, initialize_session, append_turn, build_model_packet, persist_session, run_sapiens_client, main

## Docstring
Sapiens client — packet-aware human-model interaction interface.

Builds, validates, and persists interaction packets between human operators
and the CIEL model layer.  Writes session transcripts and latest-packet
snapshots to ``integration/reports/sapiens_client/``.
