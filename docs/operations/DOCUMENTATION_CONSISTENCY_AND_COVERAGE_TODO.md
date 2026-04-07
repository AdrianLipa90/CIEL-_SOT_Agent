# OPERATION DOCUMENTATION CONSISTENCY & COVERAGE — ACTIVE TODO LEDGER

## Operational law
Before starting any phase:
- [ ] read this file in full
- [ ] confirm current repo/ref and active objective
- [ ] confirm previous phase state

After finishing any phase:
- [ ] update this file as the final step
- [ ] record completed work
- [ ] record blockers / unresolved issues
- [ ] record changed files
- [ ] record next phase readiness

Reporting protocol:
- unchanged
- progress, blockers, problem ⇄ solution, and state updates remain mandatory

---

## Project objective
Update, complete, and audit repository documentation so that documentation claims match the actual implementation state.

The operation is complete only when:
- documentation inventory is explicit,
- declaration-versus-implementation mismatches are mapped,
- high-priority stale claims are corrected,
- missing human/machine repo maps are added where needed,
- and final documentation can be treated as a trustworthy operator reference.

---

## Active input package
Primary audit seed for this operation:
- `/mnt/data/FULL_REPO_REVIEW_2026-04-07.zip`

Derived local review root:
- `/mnt/data/review_docs/FULL_REPO_REVIEW_2026-04-07`

Key seed artifacts:
- `AUDIT_FULL_PL.md`
- `CHANGESET_MANIFEST.md`
- `DECLARATION_IMPLEMENTATION_MATRIX.csv`
- `DOC_REFERENCE_GAPS.csv`
- `FILE_INVENTORY.csv`
- `HUMAN_REPO_GUIDE.md`
- `MODULE_SURFACE.json`
- `AGI_REPO_MANIFEST.json`
- `AGI_REPO_MANIFEST.yaml`
- `PROPOSED_CHANGES.patch`
- `PROPOSED_REPO_FILES/...`

---

## Current project state
- [x] operation branch created from refreshed `main`
- [x] full review package identified as primary input
- [ ] documentation inventory validated against current `main`
- [ ] declaration-versus-implementation matrix validated against current `main`
- [ ] high-priority stale docs repaired
- [ ] machine-readable repo map landed in repo
- [ ] final documentation audit gate passed

---

# PHASE A — INVENTORY / INPUT VALIDATION

## Goal
Validate the review package against the current `main` and establish the documentation surface inventory.

## A1. Branch and baseline
- [x] create active operation branch
- [x] confirm refreshed `main` baseline
- [x] identify primary input package
- [ ] record exact branch head used for operation start

## A2. Input package validation
- [x] unpack full review package locally
- [x] inspect review artifact structure
- [ ] verify package relevance against current `main`
- [ ] identify which proposed files are safe to land immediately
- [ ] identify which proposed files require fresh re-audit before landing

## A3. Documentation inventory
- [ ] validate docs inventory against current repo
- [ ] validate workflow documentation surface
- [ ] validate packaging documentation surface
- [ ] validate embedded/imported sector documentation coverage

## A4. Phase exit criteria
- [ ] input package validated against current repo
- [ ] inventory baseline explicit

---

# PHASE B — DECLARATION VS IMPLEMENTATION AUDIT

## Goal
Turn the review package into a current declaration/implementation truth map for the repo.

## B1. Claim extraction
- [ ] map top-level README claims
- [ ] map docs/INDEX claims
- [ ] map docs/OPERATIONS claims
- [ ] map workflow docs claims
- [ ] map packaging docs claims

## B2. Status classification
- [ ] classify each key claim as IMPLEMENTED
- [ ] classify each key claim as IMPLEMENTED_TRANSITIONAL
- [ ] classify each key claim as INCOMPLETE_DOC
- [ ] classify each key claim as STALE_DOC
- [ ] classify each key claim as DECLARED_FUTURE

## B3. Phase exit criteria
- [ ] current declaration/implementation matrix is explicit

---

# PHASE C — HIGH-PRIORITY DOCUMENT REPAIRS

## Goal
Land the safest, highest-value documentation fixes first.

## C1. New supporting docs
- [ ] add human repo guide
- [ ] add declaration/implementation matrix doc
- [ ] add workflow README
- [ ] add machine-readable repo maps

## C2. High-risk stale claims
- [ ] correct Sapiens client surface claims
- [ ] correct core-only tooling path claims
- [ ] correct workflow coverage claims
- [ ] correct hybrid/native/embedded repo geometry claims

## C3. Phase exit criteria
- [ ] highest-priority stale claims repaired

---

# PHASE D — PRIMARY DOC REWRITES

## Goal
Apply controlled rewrites to top-level and navigation docs after audit alignment.

## D1. Candidate rewrites
- [ ] `README.md`
- [ ] `docs/INDEX.md`
- [ ] `docs/OPERATIONS.md`

## D2. Control checks
- [ ] no path regressions introduced
- [ ] no stale entrypoint references introduced
- [ ] no overclaim beyond implementation state introduced

## D3. Phase exit criteria
- [ ] top-level documentation aligned with current repo geometry

---

# PHASE E — FINAL DOCUMENTATION AUDIT GATE

## Goal
Decide whether documentation is trustworthy enough to be treated as current system reference.

## E1. Required outputs
- [ ] inventory baseline
- [ ] declaration/implementation matrix
- [ ] changed-file log
- [ ] unresolved gap list

## E2. Final decision states
- [ ] READY_TO_CLOSE
- [ ] BLOCKED_BY_IMPLEMENTATION_DRIFT
- [ ] BLOCKED_BY_UNVERIFIED_RUNTIME_BEHAVIOR
- [ ] BLOCKED_BY_STALE_REVIEW_PACKAGE

## E3. Phase exit criteria
- [ ] final operation status recorded

---

## Current active phase
- [ ] Phase A — Inventory / Input Validation
