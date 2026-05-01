# holonomy_cosmic_seismic.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/holonomy_cosmic_seismic.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/holonomy_cosmic_seismic.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** SeriesSpec, EarthquakeSpec, HolonomyConfig
- **functions:** _ensure_datetime_index, load_scalar_series, load_earthquake_activity, bin_series, align_series, robust_standardize, preprocess_signal, analytic_phase, wrap_angle, phase_distance, white_thread_amplitude, shift_by_days, holonomic_defect, holonomy_measure, euler_closure_error, score_tau_scan, score_tau_delta_scan, save_main_plots, run_pipeline, parse_args

## Docstring
Holonomic testbed for cosmic-ray / seismic / solar coupling.

Purpose
-------
Given three time series
    1) cosmic-ray intensity (or its filtered / normalized proxy),
    2) earthquake activity,
    3) solar activity,
compute a phase-holonomy diagnostic inspired by the user's Metatime/CIEL
framewor
