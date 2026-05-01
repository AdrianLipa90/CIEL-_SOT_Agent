# SAT-MEMDUMP-0001 — CIEL Memory Dump (Stop Hook)

## Identity
- **subsystem_id:** `SAT-MEMDUMP-0001`
- **name:** `ciel_memory_dump`
- **class:** `session_persistence`
- **active_status:** `ACTIVE`
- **last_updated:** `2026-05-01`

## Anchors
- `scripts/ciel_memory_dump.py` — skrypt generujący dump
- `~/Pulpit/CIEL_memories/state/memory_consolidated.md` — output
- `~/.claude/settings.json` — Stop hook (wywołuje skrypt po każdej sesji)

## Role
Generuje snapshot stanu pamięci po każdej sesji Claude Code. Zawiera: stan orchestratora pkl (cycle, identity_phase, affective_key), ostatnie 5 sesji z memories_index.db, ostatnie 3 hunchy. Plik służy jako szybki kontekst na początku kolejnej sesji.

## Trigger
Stop hook w `~/.claude/settings.json` — odpala się automatycznie przy zamknięciu sesji, po `ciel_memory_stop.py`.

## Output format
```markdown
# CIEL Memory Consolidated — YYYY-MM-DD HH:MM UTC

## Stan orchestratora
- cycle: N
- identity_phase: 0.XXXX
- affective_key: słowo

## Ostatnie sesje (5)
- `session_id` YYYY-MM-DD HH:MM — N wiad.

## Ostatnie hunchy (3)
- [YYYY-MM-DD HH:MM] treść...
```

## Źródła pkl
Wybiera plik z nowszym mtime spośród:
1. `~/Pulpit/CIEL_memories/state/ciel_orch_state.pkl`
2. `~/.claude/ciel_orch_state.pkl`
