# _gh_utils.py — src/ciel_sot_agent/_gh_utils.py

## Identity
- **path:** `src/ciel_sot_agent/_gh_utils.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** UpstreamConfig
- **functions:** wrap_angle, _github_json, fetch_head, load_upstreams, load_runtime_state, propagate_phase_changes

## Docstring
Shared GitHub API utilities for the coupling subsystems.

Provides the ``UpstreamConfig`` dataclass, HTTP helpers, upstream loading,
runtime-state loading, and the phase-propagation algorithm that are shared
between ``gh_coupling`` (v1) and ``gh_coupling_v2``.
