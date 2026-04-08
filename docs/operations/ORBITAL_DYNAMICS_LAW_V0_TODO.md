# OPERATION ORBITAL DYNAMICS LAW V0 — ACTIVE TODO LEDGER

## Operational law
Before starting any phase:
- [ ] read this file in full
- [ ] confirm current repo/ref and active objective
- [ ] confirm predecessor handoff state

After finishing any phase:
- [ ] update this file as the final step
- [ ] record completed work
- [ ] record blockers / unresolved issues
- [ ] record changed files
- [ ] record next phase readiness
- [ ] record predecessor/successor links if the operation is split or handed off

Session handoff reference:
- `docs/operations/CIEL_REPO_WORKSTYLE_SESSION_HANDOFF.md`

Reporting protocol:
- unchanged
- progress, blockers, problem ⇄ solution, and state updates remain mandatory

---

## Predecessor operation
This operation is the direct successor to:
- [`DOCUMENTATION_CONSISTENCY_AND_COVERAGE_TODO.md`](./DOCUMENTATION_CONSISTENCY_AND_COVERAGE_TODO.md)

The documentation operation established the repo geometry, execution surfaces, packaging truth, and machine-readable repo maps needed before orbital runtime changes can be introduced safely.

---

## Project objective
Introduce **Orbital Dynamics Law v0** as an effective, discrete orbital law for stable information-bearing orbits in a relational medium, without mixing:
- analogy,
- hypothesis,
- formal executable claim,
- and runtime implementation.

The operation is complete only when:
- semantic boundaries are hardened,
- phased-state contracts are explicit,
- orbital selection is separated from raw identity phase,
- the formal spec for orbital dynamics v0 exists,
- runtime v0 law is wired in without semantic regression,
- and performance/test evidence exists for the new path.

---

## Branch and baseline
Historical branch provenance:
- `operation/orbital-dynamics-law-v0-phase-a-20260407`
- `operation/orbital-dynamics-law-v0-phase-b-20260407`
- `operation/orbital-dynamics-law-v0-phase-c-20260407`

Current normalization branch:
- `fix/post-merge-normalization-20260408`

Current `main` baseline for this normalization pass:
- `496a9e186a27693aa7454da8f5455897448b4ee5`

## Current rationale
Current `main` already contains:
- Phase A semantic boundary hardening,
- Phase B phased-state domain contracts,
- Phase C identity-phase versus selection-relevance separation,
- and the session handoff workstyle layer.

This normalization pass exists because several repo-memory surfaces still reflected branch-local state after those phases had already landed on `main`.

---

# PHASE A — SEMANTIC BOUNDARY HARDENING

## Goal
Make the boundary between analogy, science, architecture, operations, and executable runtime machine-visible and review-stable.

## Deliverables
- `docs/science/RELATIONAL_ORBITAL_DYNAMICS_SPEC_V0.md`
- `docs/analogies/KEPLER_SUPERFLUID_ANALOGIES.md`
- updated documentation classification / cross-reference layer

## Checklist
- [x] confirm document status taxonomy: `analogy`, `science`, `architecture`, `operations`, `report`, `archive`
- [x] update surviving docs index / navigation layer to reflect taxonomy
- [x] add formal orbital dynamics spec stub in `docs/science/`
- [x] add Kepler/superfluid analogies note in `docs/analogies/`
- [x] ensure analogy documents are not referenced as executable claims

## Exit criteria
- [ ] analogy and formal spec are no longer confusable in repo navigation or validation

## Phase A status on `main`
- Merged.
- Remaining open point: no automated classification/validation hook yet checks that future docs preserve the boundary.

---

# PHASE B — PHASED STATE CONTRACTS

## Goal
Make the input/domain contracts of `phased_state.py` explicit.

## Decision target
Prefer a **strict contract model** unless implementation review proves permissive wrapping is required.

## Checklist
- [x] decide strict contract for `compute_phase(h)`
- [x] decide strict contract for `f_conn(r)`
- [x] implement explicit validation in `src/ciel_sot_agent/phased_state.py`
- [x] add boundary tests in `tests/test_phased_state.py`
- [x] document the chosen domain contract

## Exit criteria
- [x] there are no silent or ambiguous domain assumptions in phased-state entry functions

## Phase B status on `main`
- Merged.
- Contract state: `compute_phase(h)` accepts only a finite real hash fraction in `[0.0, 1.0)`, and `f_conn(r)` accepts only a non-negative integer connection count.

---

# PHASE C — RELATIONAL SEED SEPARATION

## Goal
Separate identity phase from selection relevance.

## Checklist
- [x] preserve deterministic identity phase for object identity
- [x] define relational selection features (layer, provenance, crossrefs, anchors, sector role, upstream/downstream)
- [x] introduce `selection_weight` / `relational_relevance`
- [x] refit phased-state gating so amplitude/energy acts over relevance, not raw identity seed
- [x] create benchmark-style fixtures comparing identity-phase drift vs relevance-stable selection

## Exit criteria
- [ ] orbital selection correlates with relevance instead of merely with deterministic object identity

## Phase C status on `main`
- Merged.
- Resolved in code: hash-derived `h` now drives only `phi`, while selection/amplitude flows through explicit relational metadata.
- Remaining open point: the broader repo-wide audit of all possible selector surfaces is still not complete.

---

# POST-MERGE NORMALIZATION — AUDIT FOLLOW-UP

## Goal
Normalize repo-memory surfaces after Phase A/B/C landed on `main`.

## Checklist
- [x] remove stale branch-era status from `agentcrossinfo.md`
- [x] normalize orbital ledger wording from branch-local to main-canonical state
- [x] add `tests/test_phased_state.py` to `docs/INDEX.md`
- [x] remove phased-state legacy residue and stale module wording

## Exit criteria
- [x] operational memory surfaces match the actual merged state of `main`

## Normalization entry — 2026-04-08
Resolved in this patchset:
- `agentcrossinfo.md` now reflects the current audit/normalization pass instead of stale branch-era orbital planning state,
- `docs/INDEX.md` now exposes `tests/test_phased_state.py` and the active phased-state layer,
- `src/ciel_sot_agent/phased_state.py` no longer contains the unused `f_seed(h)` helper and now describes its current semantics accurately,
- this ledger now records Phase A/B/C as merged-on-main state rather than as active branch-local work.

Changed files:
- `src/ciel_sot_agent/phased_state.py`
- `docs/INDEX.md`
- `agentcrossinfo.md`
- `docs/operations/ORBITAL_DYNAMICS_LAW_V0_TODO.md`

Known limitation:
- no full suite or CI certification is recorded here for the new `main` head from within this patch flow.

---

# PHASE D — ORBITAL DYNAMICS SPEC V0

## Goal
Write the formal orbital law before changing runtime behavior.

## Minimal formal state targets
- [x] `mu_eff`
- [x] `winding`
- [x] `tau_orbit`
- [x] `phase_slip_ready`
- [x] `rho <-> q_target` relation
- [x] effective Kepler-type law `T^2 ~ rho^3 / mu_eff`
- [x] threshold/phase-slip transition rule

## Exit criteria
- [x] a short, reviewable orbital dynamics law v0 exists as formal spec

---

# PHASE E — ORBITAL LAW RUNTIME V0

## Goal
Introduce the effective orbital law into the existing orbital runtime without destroying current relacyjny dynamics.

## Target files
- `integration/Orbital/main/model.py`
- `integration/Orbital/main/metrics.py`
- `integration/Orbital/main/dynamics.py`

## Checklist
- [ ] extend `Sector` with orbital-law fields
- [ ] add effective attractor strength and period helpers
- [ ] add phase-slip readiness computation
- [ ] add optional `use_orbital_law_v0` path
- [ ] keep compatibility with current relational dynamics path

## Exit criteria
- [ ] runtime contains an effective discrete orbital law path v0

---

# PHASE F — DYNAMICS PERFORMANCE REPAIR

## Goal
Repair the real bottleneck in `step_dynamics` after semantics are fixed.

## Checklist
- [ ] profile `_relational_step()` and `_perturbed_potential()`
- [ ] remove unnecessary `deepcopy`/full recomputation patterns from gradient estimation
- [ ] replace numerical perturbation where possible with cached or analytical gradients
- [ ] repeat benchmark after changes

## Exit criteria
- [ ] performance gains come from mathematical/runtime cleanup, not from hiding the cost behind concurrency

---

# PHASE G — SEMANTIC TEST & BENCH SUITE

## Goal
Produce evidence that orbital law v0 improves runtime semantics or at least does not regress them.

## Checklist
- [ ] add orbital selection benchmarks
- [ ] add precision/recall style relevance fixtures
- [ ] add stability tests for orbit/period/threshold-jump behavior
- [ ] add tests for winding update semantics

## Exit criteria
- [ ] semantic/runtime evidence exists for the new law

---

# PHASE H — PACKAGE GEOMETRY REFACTOR (LATE)

## Goal
Refactor package geometry only after semantics and runtime law stabilize.

## Checklist
- [ ] decide target subpackage layout (`core`, `orbital`, `github`, `sapiens`, `validation`, `gui`)
- [ ] preserve compatibility imports
- [ ] migrate docs and entrypoints only after law/test layers are stable

## Exit criteria
- [ ] package geometry reflects stable semantics rather than forcing them prematurely

---

## Current active phase
- [ ] Phase E — Orbital Law Runtime V0 is the next implementation phase
- [ ] Broader selector audit outside `phased_state.py` remains an optional pre-runtime verification pass

## Immediate next action
- [ ] decide whether to enter runtime-law wiring directly or run one more repo-wide selector audit before Phase E

## Successor rule
If this operation is later split into sub-operations, every successor must link back here and record which patchset boundary it inherits.
