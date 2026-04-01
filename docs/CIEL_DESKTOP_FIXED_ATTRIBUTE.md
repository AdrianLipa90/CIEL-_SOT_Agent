# CIEL-Desktop Fixed Attribute

## Status

`CIEL-Desktop` is declared as a **fixed attribute** of `CIEL-_SOT_Agent`.

## Meaning

This does not mean that the desktop repository replaces the integration manifold.
It means the desktop surface is treated as a stable, explicit subsystem bound to the agent layer.

## Canonical declaration

The machine-readable declaration lives at:

- `integration/fixed_attributes/ciel_desktop_fixed_attribute.json`

## Binding rule

- source repository: `AdrianLipa90/CIEL-Desktop`
- target repository: `AdrianLipa90/CIEL-_SOT_Agent`
- binding mode: `fixed-attribute`
- subsystem role: `desktop-surface`

## Follow-up

A later registry refactor should fold this declaration into:
- `integration/repository_registry.json`
- `integration/couplings.json`
- `integration/gh_upstreams.json`

Until then, this file and its paired JSON declaration are the canonical statement that Desktop is a fixed attribute in SOT_Agent.
