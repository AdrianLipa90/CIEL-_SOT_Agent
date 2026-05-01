# spreadsheet_db.py — src/ciel_sot_agent/spreadsheet_db.py

## Identity
- **path:** `src/ciel_sot_agent/spreadsheet_db.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _xlsx_lock, _now_ts, _load_or_create, _ensure_sheet, _row_by_id, upsert_entity_card, append_htri_metrics, append_pipeline_metrics, append_cqcl_log, upsert_nonlocal_card, load_entity_cards, db_path

## Docstring
CIEL Spreadsheet DB — arkusze kalkulacyjne jako baza danych kart obiektów.

Każda kategoria kart to osobny arkusz w jednym pliku XLSX:
  integration/db/ciel_cards.xlsx

Arkusze:
  entity_cards   — karty bytów (id, noun, coupling, phase, horizon_class, adjectives, note)
  htri_metrics   — historia me
