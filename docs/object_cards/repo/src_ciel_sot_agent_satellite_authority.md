# satellite_authority.py — src/ciel_sot_agent/satellite_authority.py

## Identity
- **path:** `src/ciel_sot_agent/satellite_authority.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** load_satellite_authority_matrix, get_satellite_authority, require_export_surface, require_interaction_surface, require_io_stack, project_authority_summary, resolve_root

## Docstring
Authority loading and lookup for satellite subsystems.

Satellite subsystems live beyond the bridge horizon and must not silently
override canonical runtime state. This module centralizes the authority
matrix so code surfaces can read, expose, and enforce the same rules.
