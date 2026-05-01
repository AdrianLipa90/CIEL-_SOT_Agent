# ENT-system_health_formula — Formuła system_health

## Identity
- **entity_id:** `entity:system_health_formula`
- **noun:** formuła system_health
- **horizon_class:** `POROUS`

## Formalnie
system_health = (0.55·ci + 0.20·closure_score + 0.25·(1−rh_eff)) / (1 + 0.08·err)

gdzie:
- ci = coherence_index
- closure_score = euler_bridge_closure_score
- rh_eff = R_H (efektywny)
- err = liczba błędów pipeline

## Wartość referencyjna (P7 baseline, 2026-05-01)
0.626

## Historia anomalii
Spike do 0.214 wykryty w tej sesji — przyczyna: jednorazowy wpis w metrics DB z timestamp 1777589382 (rok 2026 zamiast bieżącego). Nie był realną degradacją systemu.

## Tryby wg closure_penalty
- < 5.2 → deep
- 5.2–5.8 → standard
- > 5.8 → safe
