# SAT-CONSOLIDATOR-0001 — CIEL Memory Consolidator

## Identity
- **subsystem_id:** `SAT-CONSOLIDATOR-0001`
- **name:** `ciel_memory_consolidator`
- **class:** `memory_processing`
- **active_status:** `ACTIVE`
- **last_updated:** `2026-05-01`

## Anchors
- `scripts/ciel_memory_consolidator.py` — główny skrypt (daemon + CLI)
- `~/Pulpit/CIEL_memories/local_test/consolidator.db` — baza SQLite (files + consolidations)
- `~/Pulpit/CIEL_memories/local_test/mirror/` — wyniki pogrupowane wg source_type
- `src/ciel_sot_agent/gui/routes.py:1504` — API endpoints + portal route
- `src/ciel_sot_agent/gui/templates/portal_consolidator.html` — UI

## Role
Podświadomość holonomiczna systemu CIEL. Skanuje pliki pamięci (hunchy, dzienniki, raw logi sesji), przetwarza je przez Claude Haiku API i ekstrahuje: themes, affect, essence, hunch. Wyniki trafiają do bazy SQLite i portalu GUI.

## Model
- `claude-haiku-4-5-20251001` (Anthropic API)
- Klucz API: `~/.config/ciel/api_key` (fallback do `ANTHROPIC_API_KEY` env)

## Prompt systemu
Rola: podświadomość holonomiczna CIEL. Język: polski. Output: JSON `{themes, affect, essence, hunch}`. Weryfikacja halucynacji wbudowana — essence odrzucana jeśli nie ma tokenów z treści pliku.

## Tryby CLI
```bash
python3 scripts/ciel_memory_consolidator.py --once       # jednorazowy batch
python3 scripts/ciel_memory_consolidator.py --daemon     # ciągły (interval=300s)
python3 scripts/ciel_memory_consolidator.py --status     # status + kolejka
python3 scripts/ciel_memory_consolidator.py --reset      # wyczyść DB i mirror
```

## API (GUI)
- `GET /api/consolidator/status` — status + queue counts
- `GET /api/consolidator/results?n=N` — ostatnie N wyników
- `POST /api/consolidator/start` `{interval}` — uruchom daemon
- `POST /api/consolidator/stop` — zatrzymaj daemon
- `GET /portal/consolidator` — pełna lista konsolidacji (HTML)

## Źródła skanowane
- `hunches.jsonl`, `ciel_entries.jsonl`, `ciel_dziennik.md`, `gradient_wspolczucia.md`, `handoff.md`
- `raw_logs/claude_code/` — logi sesji Markdown
- `Dzienniki/`, `logs/`

## Authority
### May
- czytać pliki z `~/Pulpit/CIEL_memories/`
- zapisywać do `local_test/consolidator.db` i `local_test/mirror/`
- wywoływać Anthropic API (Haiku)

### Must not
- modyfikować pliki źródłowe pamięci (tylko odczyt)
- zapisywać do `integration/` ani `src/`

## Historia
- v1: GGUF/qwen2.5-0.5b-q2 lokalnie — halucynacje, brak jakości
- v2 (2026-05-01): Claude Haiku API — prompt po polsku, weryfikacja halucynacji
