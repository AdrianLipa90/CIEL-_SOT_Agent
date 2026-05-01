# memory_rag.py — src/ciel_sot_agent/memory_rag.py

## Identity
- **path:** `src/ciel_sot_agent/memory_rag.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _keywords, _score, search_wave_archive, search_chat_history, build_memory_context, rd

## Docstring
CIEL Memory RAG — retrieval-augmented generation from wave_archive + chat history.

Searches memories for content relevant to the current query and returns
a context block to inject into the system prompt before model inference.

This is inference-time learning: the model sees its own memories on ev
