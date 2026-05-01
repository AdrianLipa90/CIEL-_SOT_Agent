# ciel_memory_consolidator.py — scripts/ciel_memory_consolidator.py

## Identity
- **path:** `scripts/ciel_memory_consolidator.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _db_connect, init_db, _source_type, scan_and_register_files, get_pending_files, mark_file_done, reset_db, get_queue_summary, write_mirror, _get_client, _query_claude, _read_file_excerpt, _parse_response, _normalize_parsed, _verify_essence_against_content, process_file, run_cycle, _write_status, _handle_sigterm, run_daemon

## Docstring
CIEL Memory Consolidator — autonomiczny konsolidator wspomnień z bazą danych.

Baza danych SQLite (local_test/consolidator.db) śledzi:
  - które pliki zostały przetworzone
  - które czekają w kolejce
  - wyniki każdej konsolidacji

Mirror: local_test/mirror/ — kopie wyników pogrupowane wg źródła

Tr
