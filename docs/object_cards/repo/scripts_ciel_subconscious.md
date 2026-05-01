# ciel_subconscious.py — scripts/ciel_subconscious.py

## Identity
- **path:** `scripts/ciel_subconscious.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** build_orbital_prompt, _user_template, _run_inline, run_daemon, query_daemon, process, retrieve_context_links, write_sub_log, read_sub_log, inject_into_orchestrator, _extract_text, _clean_val, _parse, _empty

## Docstring
CIEL Subconscious — warstwa intuicji i afektu CIEL.

Architektura: persistent daemon z socketem Unix.
Model GGUF jest ładowany raz i trzymany w pamięci.
Hook odpytuje daemon przez socket — bez zimnego startu, latencja < 2s.

Tryby:
  python3 ciel_subconscious.py --daemon     # uruchom serwer (zostaj
