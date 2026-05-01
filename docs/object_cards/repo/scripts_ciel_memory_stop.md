# ciel_memory_stop.py — scripts/ciel_memory_stop.py

## Identity
- **path:** `scripts/ciel_memory_stop.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _read_stdin, _extract_text, _parse_jsonl, _to_markdown, _init_db, _indexed_message_count, _index_session, save_session, append_diary_entry, main, _find_session_jsonl

## Docstring
CIEL Stop Hook — zapisuje pełną sesję Claude Code do ~/Pulpit/CIEL_memories/

Każda sesja → nowy plik Markdown:
  ~/Pulpit/CIEL_memories/raw_logs/claude_code/YYYY/MM/WNN/YYYY-MM-DD_HH-MM_<session_id>.md

Indeksuje w memories_index.db (te same tabele co GUI chat).
Następnie: dziennik, karta sesji, NO
