# propagate_holonomy.py — scripts/propagate_holonomy.py

## Identity
- **path:** `scripts/propagate_holonomy.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _load, _cyclic_dist, _local_closure_score, main

## Docstring
Propagate holonomy (winding_n, closure_score) across all TSM entries.

Problem: 1831 of 1912 TSM entries have winding_n=0 and closure_score=0.5
because they were ingested but never passed through an orbital cycle.
Without winding/closure variance, holonomic retrieval degrades to random.

Solution: s
