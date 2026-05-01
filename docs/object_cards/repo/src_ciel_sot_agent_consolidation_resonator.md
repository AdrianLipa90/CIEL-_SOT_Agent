# consolidation_resonator.py — src/ciel_sot_agent/consolidation_resonator.py

## Identity
- **path:** `src/ciel_sot_agent/consolidation_resonator.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** ConsolidationRecord, TagCard
- **functions:** normalize_tag, load_consolidations, build_tag_map, _load_phase_state, _save_phase_state, _build_coupling_matrix, _lorentz_omega, kuramoto_sync, kuramoto_order_parameter, write_tag_cards, write_to_tsm, update_encoder_from_kuramoto, _circular_mean, _circular_std, _phi_to_sector, run

## Docstring
CIEL Consolidation Resonator — średnioterminowa pamięć fazowa.

Pipeline:
  1. TAG MAPPER     — normalizacja 1502 tagów → klastry kanoniczne
  2. TAG CARDS      — karta per tag: M_sem, phi_tag, winding, sektor
  3. KURAMOTO       — sprzężenie fazowe ostatnich 400 konsolidacji
                      d
