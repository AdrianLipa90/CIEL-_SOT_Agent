# generate_site.py — scripts/generate_site.py

## Identity
- **path:** `scripts/generate_site.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** load_pipeline_report, section_ciel_omega, load_mindflow, load_intentions, load_entity_cards, load_orbital_final, load_entity_orbital, load_phase_history, _svg_sparkline, load_cache_entries, load_snapshots, load_wpm_memories, load_diary_entries, _parse_frontmatter, load_project_memory, load_object_cards, _inline, md_to_html, esc, _nav_html

## Docstring
CIEL Site Generator — generuje statyczną stronę HTML z danych CIEL.

Źródła:
  ~/.claude/ciel_mindflow.yaml     → Przemyślenia, pytania, napięcia
  ~/.claude/ciel_intentions.md     → Agenda / intencje
  ~/.claude/ciel_snapshots/        → Historia sesji
  ~/.claude/projects/.../memory/prompt_cache.md
