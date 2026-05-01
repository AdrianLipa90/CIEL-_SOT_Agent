# state_db.py — src/ciel_sot_agent/state_db.py

## Identity
- **path:** `src/ciel_sot_agent/state_db.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** get_db, _ensure_schema, save_report, load_report, load_report_freshness, append_metrics, load_metrics_history, save_orchestrator_state, load_orchestrator_state, load_holonomy, accumulate_berry, accumulate_subjective_winding, append_audit, _read_cycle_from_pickle, save_bridge_snapshot, db_path

## Docstring
Unified SQLite state store for CIEL system.

Single source of truth for: orchestrator state, M0-M8 metrics, JSON reports,
intentions, and metrics history. Replaces scattered pickle + 72 JSON files.

DB location: ~/.claude/ciel_state.db
WAL mode for concurrent read/write safety.
