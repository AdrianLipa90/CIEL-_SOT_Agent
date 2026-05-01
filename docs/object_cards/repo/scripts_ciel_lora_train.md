# ciel_lora_train.py — scripts/ciel_lora_train.py

## Identity
- **path:** `scripts/ciel_lora_train.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** OrbitalTrainer
- **functions:** holonomy_loss_torch, inject_orbital_weights, load_dataset, format_for_training, train, compute_loss

## Docstring
CIEL LoRA Training Script

Fine-tuning qwen2.5-0.5B z orbitalną inicjalizacją LoRA.

Wymaga:
  pip install torch==2.0.1+cu117 --extra-index-url https://download.pytorch.org/whl/cu117
  pip install transformers peft trl accelerate bitsandbytes

Użycie:
  python3 ciel_lora_train.py
  python3 ciel_lora
