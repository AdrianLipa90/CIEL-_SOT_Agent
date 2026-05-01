# chat_archive.py — src/ciel_sot_agent/chat_archive.py

## Identity
- **path:** `src/ciel_sot_agent/chat_archive.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _init_db, _db_register_session, _db_append_message, _session_path, _get_session_file, open_session, append, append_exchange, load_recent, load_last_session_history, _parse_log_to_history, stats

## Docstring
CIEL Chat Archive — append-only conversation log in Markdown.

Hierarchical structure:
  ~/Pulpit/CIEL_memories/raw_logs/YYYY/MM/WNN/YYYY-MM-DD_HH-MM_session.md

Never modified. Never deleted. Append only.
Each session creates one file. Each file is indexed in memories_index.db.
