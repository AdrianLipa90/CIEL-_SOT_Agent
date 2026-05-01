# ciel_dataset_build.py — scripts/ciel_dataset_build.py

## Identity
- **path:** `scripts/ciel_dataset_build.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** records_from_foundation_pack, records_from_cards, records_from_coupling_matrix, records_from_holonomy, records_from_cqcl, records_identity, _chat, build_dataset

## Docstring
CIEL LoRA Dataset Builder

Kompiluje dataset treningowy ze wszystkich źródeł CIEL:
  - CIEL_Orbital_Foundation_Pack (formalna teoria)
  - memory/cards/ (ontologia bytów)
  - coupling.py J_kj (matematyczny substrat)
  - holonomy.py (geometria Berry'ego)
  - CQCL (operatory kwantowe)

Format wyjściowy
