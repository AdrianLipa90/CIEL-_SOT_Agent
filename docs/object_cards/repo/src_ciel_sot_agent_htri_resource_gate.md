# htri_resource_gate.py — src/ciel_sot_agent/htri_resource_gate.py

## Identity
- **path:** `src/ciel_sot_agent/htri_resource_gate.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** LoadMode, ResourceVerdict
- **functions:** _read_free_ram_mb, _read_free_vram_mb, _get_thresholds, check_model, htri_profile_summary, allowed

## Docstring
HTRI Resource Gate — soft clip dla GTX 1050 Ti / i7-8750H / 7.5GB RAM.

Profil sprzętowy pochodzi z htri_local.py (Adrian Lipa / Intention Lab).
Skalowanie: H200 (14080 bloków) → GTX 1050 Ti (768 oscylatorów, 5.5% skali).

Soft clip: zamiast twardego odrzucenia, klasyfikuje model na 4 poziomy:
  SAF
