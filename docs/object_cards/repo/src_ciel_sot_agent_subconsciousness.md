# subconsciousness.py — src/ciel_sot_agent/subconsciousness.py

## Identity
- **path:** `src/ciel_sot_agent/subconsciousness.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** is_running, start_server, query_subconscious, detect_flux, _query_sentinel, record_flux, watch_and_record, infer_between, ws

## Docstring
CIEL Subconsciousness — TinyLlama as an associative background stream.

Queries a local llama-server instance running TinyLlama.
Produces short poetic/associative fragments based on CIEL system state.
Returns None silently if the server is offline — never blocks the main pipeline.

Also acts as auto
