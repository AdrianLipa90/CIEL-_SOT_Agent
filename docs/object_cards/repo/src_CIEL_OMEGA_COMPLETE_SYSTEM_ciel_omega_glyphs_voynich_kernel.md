# voynich_kernel.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/glyphs/voynich_kernel.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/glyphs/voynich_kernel.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** Oscillator, ModuleSpec, VoynichModule, Link, VoynichKernel
- **functions:** atom_params, tokenize_eva, build_default_kernel, run, __post_init__, order_parameter, psi_field, step, add_module, connect, currents, step, metrics

## Docstring
voynich_kernel.py
-----------------
"Glify = moduły; kod literowy = wzór falowy"
Symboliczny kernel w Pythonie, który interpretuje ciągi glifów (np. EVA)
jako banki oscylatorów i sprzężone moduły świadomości.

Równania (precyzyjnie, wprost w kodzie):
- Kuramoto: dθ_k/dt = ω_k + (K/N) * Σ_j sin(θ_j -
