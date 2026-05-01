# run_ciel_gguf.py — scripts/run_ciel_gguf.py

## Identity
- **path:** `scripts/run_ciel_gguf.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _pull_ciel_metrics, _orbital_mode, _build_geometry_prompt, _find_model, main, _reply

## Docstring
run_ciel_gguf.py — CIEL geometry + semantic algorithm injected into local GGUF.

Usage:
    python scripts/run_ciel_gguf.py [--model PATH] [--prompt TEXT]

Pulls live CIEL metrics from the pipeline, builds a geometric system prompt
(Kähler manifold state, Berry holonomy, L_rel, orbital mode), and ru
