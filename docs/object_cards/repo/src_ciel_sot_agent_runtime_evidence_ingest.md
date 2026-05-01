# runtime_evidence_ingest.py — src/ciel_sot_agent/runtime_evidence_ingest.py

## Identity
- **path:** `src/ciel_sot_agent/runtime_evidence_ingest.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** ValidationIssue
- **functions:** load_json_file, validate_runtime_evidence_data, classify_evidence, ingest_runtime_evidence, main

## Docstring
Runtime evidence ingest pipeline for CIEL-SOT-Agent.

Reads structured evidence artefacts (schemas, reports, registry files) from
the ``integration/`` directory, validates them against known schemas, and
writes a consolidated ``runtime_evidence_ingest.json`` report consumed by
the Sapiens interactio
