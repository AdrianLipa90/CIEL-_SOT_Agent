# import_chatgpt_logs.py — scripts/import_chatgpt_logs.py

## Identity
- **path:** `scripts/import_chatgpt_logs.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _init_db, _already_imported, _save_session, _save_messages, _ts, _extract_text, _walk_thread, _week_label, _conversation_to_markdown, _import_conversation, _load_conversations, main, walk

## Docstring
Import ChatGPT conversation export into CIEL memory archive.

Usage:
    python3 scripts/import_chatgpt_logs.py /path/to/conversations.json
    python3 scripts/import_chatgpt_logs.py /path/to/chatgpt_export.zip

ChatGPT export: Settings → Data controls → Export data → conversations.json
The script a
