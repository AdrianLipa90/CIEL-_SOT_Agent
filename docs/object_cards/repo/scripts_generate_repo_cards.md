# generate_repo_cards.py — scripts/generate_repo_cards.py

## Identity
- **path:** `scripts/generate_repo_cards.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _extract_py_info, _card_path, _write_py_card, _write_json_card, _write_index, main

## Docstring
Automatyczny generator kart obiektów dla repo CIEL.
Skanuje src/**/*.py i kluczowe JSONy, generuje/aktualizuje karty w docs/object_cards/repo/.
Uruchamiany: ręcznie, z hooka post-commit, lub ze Stop hooka.
