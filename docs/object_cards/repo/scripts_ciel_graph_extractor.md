# ciel_graph_extractor.py — scripts/ciel_graph_extractor.py

## Identity
- **path:** `scripts/ciel_graph_extractor.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** Entity, Relation
- **functions:** extract_entities, extract_relations, update_subject_file, update_graph_index, process_report, run_live, main

## Docstring
CIEL Graph Extractor — draft/experimental

Wyciąga podmioty i relacje z artykułów RSS i aktualizuje NEWS/GRAPH.md + subjects/*.md.

Słownik znaczeń, nie prawdopodobieństw:
  - węzeł = podmiot (państwo, osoba, organizacja, koncepcja)
  - krawędź = relacja (CONFLICT_WITH, ALLIED_WITH, NEGOTIATES_WITH,
