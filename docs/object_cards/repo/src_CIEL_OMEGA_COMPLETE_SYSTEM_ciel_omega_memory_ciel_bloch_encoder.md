# ciel_bloch_encoder.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/ciel_bloch_encoder.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/memory/ciel_bloch_encoder.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** BlochState, BlochEncoderResult, _TSMCache, CIELBlochEncoder
- **functions:** _load_orbital_mass_table, _build_noun_index, _load_berry_accumulated, _load_cqcl_phase, _tokenize, _token_mass, _load_sector_weights, _init_sector_weights, phasor, bloch_vector, __post_init__, __init__, _load, get, __init__, encode, _tokens_to_bloch, _weighted_pool, _blend_phases, _sector_distribution

## Docstring
CIEL Bloch Encoder — własny encoder od zera.

Architektura:
    token → lookup TSM (phi_berry, winding_n, D_type) → M_sem(token)
          → stan Blocha: |ψ⟩ = cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩
          → ważony pool: Σ M_sem_i · |ψ_i⟩ / Σ M_sem_i
          → projekcja CP¹ → φ_text
          → blend:
