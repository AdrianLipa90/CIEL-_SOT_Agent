# orch_orbital.py — src/ciel_sot_agent/orch_orbital.py

## Identity
- **path:** `src/ciel_sot_agent/orch_orbital.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** load_entity_cards, entity_orbital_summary, _entity_sector_name, _rho_from_theta, _card_to_sector_dict, _phase_coupling, build_entity_injection, entity_orbital_metrics, run_entity_mini_pass, dynamic_adjectives, enrich_entity_cards_with_dynamics

## Docstring
OrchOrbital — CIEL entity cards reader, orbital metrics exporter,
and entity sector injector for the orbital bridge.

Loads ciel_entity_cards.yaml and:
  1. Exposes entity coupling/phase metrics for SessionStart context.
  2. Injects entity cards as Sector nodes into the OrbitalSystem,
     enabling
