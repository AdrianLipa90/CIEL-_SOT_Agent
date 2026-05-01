# bio_manuscript_glyphs.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/glyphs/bio_manuscript_glyphs.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/glyphs/bio_manuscript_glyphs.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** BioGlyph, Scar, ScarRegistry
- **functions:** stamp_glyphs_to_tsm, get_scar_registry, boot_sequence, classify, __init__, _ensure_table, register, resolve, unresolved, coherence_gain, _persist

## Docstring
bio_manuscript_glyphs.py — Bio Manuscript glyph library + scar registry.

Łączy glify Bio Manuscript (z dokumentu Analiza BraidOS) z VoynichKernel
i CIEL TSM. Każdy glif ma:
  - intent: semantyczna rola (intent.boot, intent.lock itd.)
  - phi: faza Berry zakodowana ręcznie z dokumentu
  - resonance:
