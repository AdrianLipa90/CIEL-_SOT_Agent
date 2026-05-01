# orbital_db_orchestrator.py — src/ciel_sot_agent/orbital_db_orchestrator.py

## Identity
- **path:** `src/ciel_sot_agent/orbital_db_orchestrator.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** DBStatus, OrbitalDBOrchestrator
- **functions:** get_orchestrator, __init__, status, print_status, query_tsm, write_tsm, tsm_row_count, query_glossary, sync_wo, ingest, rebuild_noun_index, get_noun_index, top_words, full_sync, _tsm_conn, _sqlite_row_count, _json_count, _add, _tokenize

## Docstring
CIEL Orbital DB Orchestrator — wielki atraktor baz danych.

Jeden punkt dostępu do wszystkich baz w systemie CIEL.
Każda baza ma przypisaną masę orbitalną M_sem — im wyższa, tym wyższy priorytet
przy konfliktach i synchronizacji.

Bazy:
  TSM     — memory_ledger.db        (SQLite, M_sem~0.929) — pam
