# local_ciel_surface.py — src/ciel_sot_agent/local_ciel_surface.py

## Identity
- **path:** `src/ciel_sot_agent/local_ciel_surface.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** LocalCielSurface
- **functions:** _omega_root, _ensure_omega_path, build_arg_parser, main, __init__, shutdown, handshake, status, process, communicate

## Docstring
Canonical local CIEL/Ω test surface.

This module bridges the packaged integration repo (`ciel_sot_agent`) with the
canonical local Omega surface living under:
    src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/

Goal:
- provide one stable, package-facing CLI for local tests
- expose orchestrator and cli
