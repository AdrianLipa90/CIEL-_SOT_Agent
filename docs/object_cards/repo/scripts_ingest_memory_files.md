# ingest_memory_files.py — scripts/ingest_memory_files.py

## Identity
- **path:** `scripts/ingest_memory_files.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _load_direct, _chunks, parse_md, parse_txt, parse_json, parse_jsonl, parse_yaml, parse_pdf, parse_docx, parse_db, collect_files, already_ingested, main

## Docstring
Ingest all memory files (md, txt, json, jsonl, yaml, pdf, docx, db) into TSM.

Parses each file into text chunks, encodes with CIELEncoder → phi_berry,
then stamps into holonomic_memory TSM (only new entries, never overwrites).

Usage:
    python3 scripts/ingest_memory_files.py [--dry-run] [--source
