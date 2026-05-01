# manager.py — src/ciel_sot_agent/gguf_manager/manager.py

## Identity
- **path:** `src/ciel_sot_agent/gguf_manager/manager.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** ModelSpec, GGUFManager
- **functions:** _default_models_dir, _sha256_file, get_model_path, download_default_model, __init__, list_models, is_installed, model_path, ensure_model, save_manifest, load_manifest, _download

## Docstring
GGUF model manager — download and locate small quantised models on first startup.

The manager is intentionally lightweight: it uses only Python stdlib so that the
core package does not require heavy ML dependencies at install time.  The actual
model runner (llama.cpp, ctransformers, etc.) is left t
