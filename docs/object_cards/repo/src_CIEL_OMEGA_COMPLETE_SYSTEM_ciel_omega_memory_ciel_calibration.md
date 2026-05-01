# ciel_calibration.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/ciel_calibration.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/ciel_calibration.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** CIELCalibration
- **functions:** calibrate, get_calibration, _compute, _optimal_k, _inter_write_interval, _fallback, to_dict, _norm_entropy

## Docstring
CIEL Calibration — emergent parameter inference from TSM.

Philosophy: no hardcoded constants. Every parameter is a measurement of the
living TSM distribution. The system calibrates itself from what it has learned.

    φ is relational, not absolute.
    Weights are eigenvectors, not design choices.
