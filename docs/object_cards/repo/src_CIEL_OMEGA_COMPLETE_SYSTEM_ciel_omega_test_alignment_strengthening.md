# test_alignment_strengthening.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/test_alignment_strengthening.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/test_alignment_strengthening.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** test_alignment_strengthening

## Docstring
Test if strengthening α_k improves D_id monotonicity

Current issue: D_id increases in ~25% of random initial conditions.
Hypothesis: α_k (alignment cost) is too weak relative to β_kj (conflict).
Solution: Multiply α_k by factor > 1 to prioritize identity alignment.
