# ciel_memory_dump.py — scripts/ciel_memory_dump.py

## Identity
- **path:** `scripts/ciel_memory_dump.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _load_orch_summary, _load_hunches, _load_recent_sessions, generate, main

## Docstring
CIEL Memory Dump — generuje memory_consolidated.md przy końcu sesji.

Zawiera: aktualny stan orchestratora (pkl), ostatnie hunchy, ostatnie wpisy z memories_index.db.
Uruchamiany ze Stop hooka (po ciel_memory_stop.py).
