# information_flow.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/integration/information_flow.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/integration/information_flow.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** InformationFlow
- **functions:** step

## Docstring
CIEL/Ω — High-level information flow pipeline.

Stitches bio, emotion, field and memory into a reproducible pipeline.
Single step() method: sensor signal → filter → intention → emotion → memory.

Cross-references:
  bio/           → EEGProcessor, CrystalFieldReceiver
  emotion/       → EmotionCore, 
