# ciel_collatz_router.py — scripts/ciel_collatz_router.py

## Identity
- **path:** `scripts/ciel_collatz_router.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** collatz_steps, euler_collatz_slot, _get_llm, route_and_generate

## Docstring
CIEL Collatz-Euler Orbital Router

Routing między trzema modelami oparty na:
  1. Fazie Eulera: z = e^(i·θ) gdzie θ = identity_phase
  2. Sekwencji Collatza: n → konwergencja do 1
  3. Liczbie kroków Collatza: c = steps(n) → slot = c % 3

Modele:
  slot 0: qwen05    — szybki, podświadomość, intuicja
