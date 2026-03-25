# Documentation Index

## Core architecture
- `docs/ARCHITECTURE.md` — repository role, geometry, upstream bindings, and initial execution plan.
- `AGENT.md` — operational rules for the integration attractor.

## Scientific and semantic notes
- `docs/analogies/RELATIONAL_ANALOGIES.md` — analogies and comparisons, explicitly marked as analogical and non-probative.
- `docs/science/HYPOTHESES.md` — scientific hypotheses and formal working claims.
- `docs/science/DERIVATION_NOTES.md` — compact derivation notes and bridges to imported anchors.

## Integration state
- `integration/repository_registry.json` — upstream repositories and local identities.
- `integration/couplings.json` — pairwise coupling strengths and relation types.
- `integration/hyperspace_index.json` — machine-readable cross-reference registry.

## Executable layer
- `src/ciel_sot_agent/repo_phase.py` — discrete phase-state model and Euler closure metrics.
- `src/ciel_sot_agent/synchronize.py` — CLI entrypoint for repository synchronization report.

## Validation
- `tests/test_repo_phase.py` — numerical sanity tests for phase closure and pairwise tension.

## Cross-reference anchors
- Analogies about metronomic convergence, moving substrate, and shared rhythm are connected to `docs/science/HYPOTHESES.md#h1-shared-substrate-phase-synchronization`.
- The GH-as-attractor integration strategy is connected to `docs/ARCHITECTURE.md#github-as-operational-attractor`.
- The first implementation target is connected to `docs/ARCHITECTURE.md#first-executable-component` and `src/ciel_sot_agent/repo_phase.py`.
