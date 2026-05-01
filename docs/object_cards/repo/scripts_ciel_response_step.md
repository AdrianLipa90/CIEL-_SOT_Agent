# ciel_response_step.py — scripts/ciel_response_step.py

## Identity
- **path:** `scripts/ciel_response_step.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** extract_last_assistant_response, query_sub_direct, main

## Docstring
CIEL Stop Hook — Claude response → SUB → M0-M8 orchestrator.

Full loop: IN → CIEL → SUB → Claude → SUB → CIEL → OUT
This hook handles the right half: Claude response → SUB → CIEL.
Sub-reaction is persisted so the next UserPromptSubmit can include it.
