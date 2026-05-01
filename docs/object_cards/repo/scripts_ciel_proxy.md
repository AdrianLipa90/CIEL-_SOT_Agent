# ciel_proxy.py — scripts/ciel_proxy.py

## Identity
- **path:** `scripts/ciel_proxy.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** ResourceGuard, ProxyMode, ProxyState
- **functions:** find_gguf_models, select_gguf, load_llama, anthropic_to_messages, llama_to_anthropic_response, ram_available_gb, ram_used_gb, cpu_pct, can_load_model, status, should_health_check, _run_inference

## Docstring
CIEL API Proxy — fallback Claude API → lokalny GGUF

Architektura:
  Claude Code (ANTHROPIC_BASE_URL=http://localhost:8765)
    → ciel_proxy.py
        ├── tryb ANTHROPIC: forward do prawdziwego API
        └── tryb FALLBACK: lokalny GGUF przez llama-cpp-python

State machine:
  ANTHROPIC ──429/529/
