# index_validator.py — src/ciel_sot_agent/index_validator.py

## Identity
- **path:** `src/ciel_sot_agent/index_validator.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** ValidationIssue
- **functions:** load_index_registry, load_json_file, validate_demo_shell_inventory_data, validate_demo_shell_map_data, validate_index_registry, main

## Docstring
Machine-readable index validator (v1) for the CIEL integration layer.

Validates the canonical index JSON file against a known schema, checks that
every referenced source file exists on disk, and emits a structured
validation report consumed by the Sapiens panel and CI tooling.
