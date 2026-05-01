# ciel_local.py — scripts/ciel_local.py

## Identity
- **path:** `scripts/ciel_local.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** load_orchestrator, build_ciel_system_prompt, run, main

## Docstring
CIEL Local — lokalny model GGUF z CUDA jako offline fallback lub autonomiczny agent.

Użycie:
    python3 ciel_local.py "twoja wiadomość"
    echo "wiadomość" | python3 ciel_local.py
    python3 ciel_local.py --model tinyllama  # (domyślny)
    python3 ciel_local.py --model qwen05     # Qwen2.5-0.5B
