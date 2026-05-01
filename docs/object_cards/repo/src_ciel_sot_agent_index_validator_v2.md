# index_validator_v2.py — src/ciel_sot_agent/index_validator_v2.py

## Identity
- **path:** `src/ciel_sot_agent/index_validator_v2.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** ValidationIssue
- **functions:** load_index_registry, load_json_file, resolve_existing_path, resolve_index_registry_path, find_demo_shell_map_object, validate_demo_shell_inventory_data, validate_demo_shell_map_data, validate_index_registry, main

## Docstring
Machine-readable index validator v2 for the CIEL integration layer.

Extends the v1 validator with v2 schema support, coupling-aware validation,
and enriched diagnostic output.  Produces a versioned report written to
``integration/reports/index_validation_v2/``.
