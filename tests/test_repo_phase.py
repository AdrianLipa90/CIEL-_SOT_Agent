from __future__ import annotations

import json
from pathlib import Path

from src.ciel_sot_agent.repo_phase import (
    RepositoryState,
    build_sync_report,
    closure_defect,
    pairwise_tension,
)


def test_closure_defect_zero_for_aligned_states() -> None:
    states = [
        RepositoryState('a', 'A', 0.0, 0.5, 1.0, 'x', 'u'),
        RepositoryState('b', 'B', 0.0, 0.5, 2.0, 'x', 'u'),
    ]
    assert abs(closure_defect(states)) < 1e-12


def test_pairwise_tension_nonnegative() -> None:
    a = RepositoryState('a', 'A', 0.0, 0.5, 1.0, 'x', 'u')
    b = RepositoryState('b', 'B', 1.0, 0.5, 1.0, 'x', 'u')
    assert pairwise_tension(a, b, 0.8) >= 0.0


def test_build_sync_report_smoke(tmp_path: Path) -> None:
    registry = {
        'repositories': [
            {'key': 'a', 'identity': 'A', 'phi': 0.0, 'spin': 0.5, 'mass': 1.0, 'role': 'r', 'upstream': 'u'},
            {'key': 'b', 'identity': 'B', 'phi': 0.0, 'spin': 0.5, 'mass': 1.0, 'role': 'r', 'upstream': 'u'},
        ]
    }
    couplings = {'couplings': {'a': {'b': 1.0}, 'b': {'a': 1.0}}}
    reg_path = tmp_path / 'registry.json'
    coup_path = tmp_path / 'couplings.json'
    reg_path.write_text(json.dumps(registry), encoding='utf-8')
    coup_path.write_text(json.dumps(couplings), encoding='utf-8')
    report = build_sync_report(reg_path, coup_path)
    assert report['repository_count'] == 2
    assert abs(report['closure_defect']) < 1e-12
    assert len(report['pairwise_tensions']) == 2
