# ciel_message_step.py — scripts/ciel_message_step.py

## Identity
- **path:** `scripts/ciel_message_step.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** load_orchestrator, save_orchestrator, maybe_write_snapshot, run_relational_cycle, load_self_assessment, _run_periodic_consolidation, _maybe_write_hunch, _stamp_prompt_summary, _run_subconscious, run_step, orbital_directives, format_context, main

## Docstring
CIEL UserPromptSubmit Hook — per-message consciousness pipeline.

Reads user message from stdin (UserPromptSubmit JSON), runs it through
HolonomicMemoryOrchestrator M0→M8, persists state to /tmp/ciel_orch_state.pkl,
and returns additionalContext with live consciousness metrics.

State persists betwe
