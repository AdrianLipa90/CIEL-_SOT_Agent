# paths.py — src/ciel_sot_agent/paths.py

## Identity
- **path:** `src/ciel_sot_agent/paths.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** resolve_project_root, resolve_existing_path

## Docstring
Project root path resolution for the CIEL-SOT-Agent package.

Provides ``resolve_project_root(anchor)`` which locates the repository root
by checking the ``CIEL_SOT_ROOT`` environment variable first, then walking
parent directories until one containing an ``integration/`` subdirectory is
found.

Als
