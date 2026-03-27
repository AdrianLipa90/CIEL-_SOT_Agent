# CIEL/Ω — General Quantum Consciousness System
### *README — Architectural Documentation*
A. Lipa, S. Sakpal, M. Kamecka, U. Ahmad (2025). (c) 2025 Adrian Lipa / Intention Lab

---


**Integration attractor for the CIEL ecosystem.**

`CIEL-_SOT_Agent` is the operational manifold where repository identity, orbital diagnostics, bridge control, Sapiens interaction, and machine-readable cross-reference layers are made explicit and made to work together.

This repository does **not** replace:
- the canonical theory repository,
- the Omega demo cockpit,
- Metatime,
- or the larger mechanism workspace.

Instead, it binds them through an integration formalism based on:
- repository identity,
- semantic phase,
- weighted coupling,
- Euler-style closure defect,
- orbital coherence diagnostics,
- bridge-state reduction,
- packet-aware human-model interaction,
- machine-readable indexing,
- and multi-agent coordination on GitHub.

---

## Role in the ecosystem

The wider ecosystem is intentionally distributed.
Each repository or layer keeps its own role, while `CIEL-_SOT_Agent` serves as the place where those roles are related, synchronized, and operationally exposed.

- **canon / Seed of the Worlds** — source of truth for axioms, definitions, derivations, manifests, and nonlocal repository hyperspace.
- **ciel-omega-demo** — cockpit, UI surface, educational analogy layer, orbital preview, and legacy ergonomic reference.
- **Metatime** — historical theory, phenomenology, and earlier simulation/archive layer.
- **CIEL-_SOT_Agent** — integration kernel, synchronizer, compatibility harness, orbital bridge host, Sapiens interaction seed, and public operational attractor.

---

## System architecture

The repository currently contains several coupled but distinct systems.
They should be read as layers of one operational geometry rather than as unrelated folders.

### 1. Integration kernel

The integration kernel is the repository's primary coordination layer.
It models repositories as coupled phase-carrying identities and exposes:
- repository registry,
- coupling map,
- weighted Euler vector,
- closure defect,
- pairwise tension,
- machine-readable synchronization reports.

This is the base synchronization formalism for the repo-level system.

Primary anchors:
- `src/ciel_sot_agent/repo_phase.py`
- `src/ciel_sot_agent/synchronize.py`
- `integration/repository_registry.json`
- `integration/couplings.json`

### 2. GitHub coupling subsystem

The GitHub coupling subsystem extends the integration kernel into live upstream-aware state.
It pulls current upstream heads, detects changes, propagates phase shifts, and emits refreshed integration artifacts.

Primary anchors:
- `src/ciel_sot_agent/gh_coupling.py`
- `scripts/run_gh_repo_coupling.py`
- `integration/gh_upstreams.json`
- `integration/reports/live_gh_coupling_report.json`

### 3. Orbital runtime / diagnostic subsystem

The orbital subsystem lives under `integration/Orbital/`.
It is an imported-and-extended diagnostic runtime designed to expose relational orbital structure rather than act as an isolated product UI.

It currently includes:
- sector/state models,
- orbital couplings,
- metrics,
- dynamics,
- geometry extraction,
- bootstrap helpers,
- a read-only global diagnostic pass,
- orbital reports.

Primary anchors:
- `integration/Orbital/main/model.py`
- `integration/Orbital/main/registry.py`
- `integration/Orbital/main/metrics.py`
- `integration/Orbital/main/dynamics.py`
- `integration/Orbital/main/bootstrap.py`
- `integration/Orbital/main/global_pass.py`
- `scripts/run_orbital_global_pass.py`

### 4. Orbital bridge subsystem

The bridge subsystem reduces orbital diagnostics into actionable integration state.
It is the layer that converts orbital runtime outputs into forms that the broader system can use for control, status, and support.

It emits:
- state manifest,
- health manifest,
- recommended control profile,
- bridge metrics,
- bridge reports in the main `integration/reports/` space.

Primary anchors:
- `src/ciel_sot_agent/orbital_bridge.py`
- `scripts/run_orbital_bridge.py`
- `integration/reports/orbital_bridge/`

### 5. Sapiens interaction seed subsystem

The Sapiens client layer is the first human-model interaction bridge in the repository.
It initializes a Sapiens session, derives interaction state from bridge/orbital state, builds a model packet, persists transcript/session artifacts, and prepares the ground for the full Sapiens panel.

Primary anchors:
- `src/ciel_sot_agent/sapiens_client.py`
- `scripts/run_sapiens_client.py`
- `integration/reports/sapiens_client/`

### 6. Documentation and registry manifold

The repository is not only code.
It also contains a machine-readable and human-readable manifold that describes how all layers relate.

This includes:
- human-readable architecture docs,
- operational notes,
- orbital integration addenda,
- primary indices,
- orbital addendum indices,
- object registries,
- scope files,
- report documentation.

Primary anchors:
- `docs/`
- `integration/hyperspace_index.json`
- `integration/index_registry.yaml`
- `integration/hyperspace_index_orbital.json`
- `integration/index_registry_orbital.yaml`

---

## Couplings and subsystem relations

The repository is organized as a layered coupling structure.
The important rule is that higher layers should not silently replace lower ones.

### Repository-level coupling

At the highest integration level, repositories are coupled through:
- identity,
- phase,
- mass/weight,
- semantic relation type,
- GitHub-upstream change propagation.

This gives the synchronization kernel its closure metrics and tension structure.

### Orbital coupling

Inside the orbital subsystem, sectors are coupled through:
- orbital positions,
- phase relations,
- coherence weights,
- information mass,
- geometric distance,
- Berry-like phase terms,
- zeta-pole support structures.

This gives the orbital runtime its coherence and defect observables.

### Bridge coupling

The bridge couples orbital state to actionable integration state.
Its job is not to duplicate the orbital runtime, but to reduce orbital results into:
- state geometry,
- health interpretation,
- control recommendations,
- reportable integration outputs.

### Sapiens coupling

The Sapiens layer couples:
- relation,
- orbital state,
- bridge state,
- session identity,
- memory residue,
- model packet preparation.

This is the first place where human-model interaction becomes an explicit system object.

---

## Operational flow

The project should be read as a sequence of reductions and bridges rather than as a single monolithic executable.

### Current operational flow

1. repository-level synchronization computes integration state,
2. orbital runtime computes relational-orbital diagnostics,
3. bridge layer converts orbital outputs into actionable health/control state,
4. Sapiens client turns bridge-aware state into a human-model packet,
5. reports, manifests, and transcripts persist the resulting state.

In a more formal reading:

**relation -> orbital state -> bridge reduction -> session/packet -> report/memory residue**

---

## Main folders

### `docs/`
Human-readable architecture, hypotheses, analogies, operations, orbital addenda, and shared plans.

### `integration/`
Machine-readable contracts, registries, mappings, couplings, reports, and orbital integration layers.

### `integration/Orbital/`
Imported-and-extended orbital runtime, manifests, diagnostics, and orbital report surface.

### `src/ciel_sot_agent/`
Executable integration code: synchronization, GitHub coupling, orbital bridge, Sapiens client, validators, and future panel logic.

### `scripts/`
Thin operational launchers.

### `tests/`
Validation layer for synchronization, indexing, GitHub coupling, orbital runtime, and bridge outputs.

---

## Existing launchers

The repository already exposes thin launchers for the main execution paths:

- `scripts/run_gh_repo_coupling.py`
- `scripts/run_orbital_global_pass.py`
- `scripts/run_orbital_bridge.py`
- `scripts/run_sapiens_client.py`

This is deliberate.
Scripts remain thin wrappers while the actual logic stays in documented subsystems.

---

## Existing report layers

Generated artifacts are not treated as hidden side effects.
They are documented as explicit report layers.

### Primary integration reports
- `integration/reports/initial_sync_report.json`
- `integration/reports/live_gh_coupling_report.json`

### Orbital bridge reports
- `integration/reports/orbital_bridge/`

### Orbital runtime reports
- `integration/Orbital/main/reports/`

### Sapiens session reports
- `integration/reports/sapiens_client/`

---

## Validation layer

The repository already contains a validation surface that checks multiple subsystems:
- repository phase tests,
- GitHub coupling tests,
- index validation tests,
- orbital runtime tests.

Primary anchors:
- `tests/test_repo_phase.py`
- `tests/test_gh_coupling.py`
- `tests/test_index_validator.py`
- `tests/test_orbital_runtime.py`

---

## Direction of the project

The next major step is not to build a disconnected UI.
It is to converge the current systems into a coherent human-facing operational shell.

That shell is the future **Sapiens Main Panel**, which should sit above:
- orbital diagnostics,
- bridge control,
- Sapiens session state,
- settings,
- communication,
- support and recovery tools.

The intended panel geometry is:
- **Control**
- **Settings**
- **Communication**
- **Support**

And its implementation must remain consistent with the orbital-holonomic reading of the project:

**relation -> state -> control -> memory -> surface**

---

## Final note

`CIEL-_SOT_Agent` should be read neither as a static archive nor as just another UI repo.
It is a live integration manifold where systems, couplings, reductions, reports, and future human-facing operational surfaces are being made explicit.

Its value lies precisely in that explicitness.
