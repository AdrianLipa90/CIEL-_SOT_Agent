"""Orbital bridge — runs the global orbital coherence pass and writes
bridge state, health, and control-recommendation manifests.

Connects the CIEL integration kernel to the Orbital diagnostic subsystem
living under ``integration/Orbital/``, ensuring phase-coherence and
resource health are reported at each synchronisation cycle.

After the orbital physics pass the bridge routes the resulting state through
the CIEL/Ω consciousness pipeline (``ciel_pipeline.run_ciel_pipeline``) so
that emotional, ethical, and soul-invariant metrics are embedded in every
report alongside the raw geometry.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from integration.Orbital.main.bootstrap import ensure_orbital_manifests, ensure_orbital_report_dirs
from integration.Orbital.main.global_pass import run_global_pass
from integration.Orbital.main.phase_control import build_health_manifest, build_state_manifest, recommend_control
from .paths import resolve_project_root

_LOG = logging.getLogger(__name__)

BRIDGE_DIR = Path('integration') / 'reports' / 'orbital_bridge'
DEFINITIONS_DIR = Path('integration') / 'registries' / 'definitions'


def _load_json_if_exists(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        _LOG.warning("Could not load %s: %s", path, exc)
        return None


def _build_sync_manifest(root: Path) -> dict[str, Any]:
    defs_root = root / DEFINITIONS_DIR
    sync_registry = _load_json_if_exists(defs_root / 'subsystem_sync_registry.json') or {}
    sync_report = _load_json_if_exists(defs_root / 'subsystem_sync_report.json') or {}
    orbital_report = _load_json_if_exists(defs_root / 'orbital_assignment_report.json') or {}
    horizon_policy = _load_json_if_exists(defs_root / 'horizon_policy_matrix.json') or {}

    boards = sync_registry.get('records', [])
    board_preview = [
        {
            'board_card_id': board.get('board_card_id'),
            'tau_orbit': board.get('tau_orbit'),
            'tau_system': board.get('tau_system'),
            'member_count': board.get('member_count'),
            'board_export_result': board.get('board_export_result'),
            'aggregation_model': board.get('aggregation_model'),
        }
        for board in boards[:5]
    ]
    classes = (horizon_policy.get('classes') or {})
    export_boundary_policy = {
        horizon_class: {
            'privacy_constraint': payload.get('privacy_constraint'),
            'leak_channel_mode': payload.get('leak_channel_mode'),
            'leak_budget_class': payload.get('leak_budget_class'),
            'exportable_fields': payload.get('exportable_fields', []),
        }
        for horizon_class, payload in classes.items()
    }
    return {
        'schema': 'ciel-sot-agent/subsystem-sync-manifest/v0.1',
        'sync_registry_present': bool(sync_registry),
        'sync_report_present': bool(sync_report),
        'board_count': sync_report.get('board_count', len(boards)),
        'avg_members_per_board': sync_report.get('avg_members_per_board', 0.0),
        'tau_orbit_count': sync_report.get('tau_orbit_count', 0),
        'tau_system_count': sync_report.get('tau_system_count', 0),
        'sync_law_counts': sync_report.get('sync_law_counts', {}),
        'condensation_operator_counts': sync_report.get('condensation_operator_counts', {}),
        'sync_scope_counts': sync_report.get('sync_scope_counts', {}),
        'privacy_constraint_counts': orbital_report.get('privacy_constraint_counts', {}),
        'horizon_class_counts': orbital_report.get('horizon_class_counts', {}),
        'export_boundary_policy': export_boundary_policy,
        'board_preview': board_preview,
    }


def _build_runtime_gating(sync_manifest: dict[str, Any]) -> dict[str, Any]:
    privacy_counts = sync_manifest.get('privacy_constraint_counts', {}) or {}
    horizon_counts = sync_manifest.get('horizon_class_counts', {}) or {}
    board_count = int(sync_manifest.get('board_count', 0) or 0)
    tau_system_count = int(sync_manifest.get('tau_system_count', 0) or 0)
    dominant_privacy = max(privacy_counts.items(), key=lambda kv: kv[1])[0] if privacy_counts else 'UNKNOWN'
    dominant_horizon = max(horizon_counts.items(), key=lambda kv: kv[1])[0] if horizon_counts else 'UNKNOWN'
    return {
        'schema': 'ciel-sot-agent/runtime-gating/v0.1',
        'dominant_privacy_constraint': dominant_privacy,
        'dominant_horizon_class': dominant_horizon,
        'export_boundary_mode': 'PROJECTED_ONLY',
        'private_state_export_allowed': False,
        'board_sync_ready': board_count > 0,
        'system_tau_coherent': tau_system_count <= 1,
        'requires_projection_operator': True,
    }


def _bridge_markdown(summary: dict[str, Any]) -> str:
    lines = [
        '# Orbital Bridge Report', '', '## Source',
        f"- source_report: {summary['source_report']}",
        f"- engine: {summary['orbital_run'].get('engine', 'unknown')}",
        f"- steps: {summary['orbital_run'].get('steps', 0)}", '', '## State Manifest',
    ]
    for key, value in summary['state_manifest'].items():
        lines.append(f'- {key}: {value}')
    lines += ['', '## Health Manifest']
    for key, value in summary['health_manifest'].items():
        lines.append(f'- {key}: {value}')
    lines += ['', '## Recommended Control']
    for key, value in summary['recommended_control'].items():
        lines.append(f'- {key}: {value}')
    lines += ['', '## Bridge Metrics']
    for key, value in summary['bridge_metrics'].items():
        lines.append(f'- {key}: {value}')
    sync_manifest = summary.get('subsystem_sync_manifest', {})
    if sync_manifest:
        lines += ['', '## Subsystem Sync Manifest']
        for key in ['board_count', 'avg_members_per_board', 'tau_orbit_count', 'tau_system_count']:
            lines.append(f'- {key}: {sync_manifest.get(key)}')
    runtime_gating = summary.get('runtime_gating', {})
    if runtime_gating:
        lines += ['', '## Runtime Gating']
        for key, value in runtime_gating.items():
            if key != 'schema':
                lines.append(f'- {key}: {value}')
    ciel = summary.get('ciel_pipeline', {})
    if ciel:
        lines += ['', '## CIEL Pipeline']
        for key, value in ciel.items():
            lines.append(f'- {key}: {value}')
    return '\n'.join(lines)


def build_orbital_bridge(root: str | Path) -> dict[str, Any]:
    root = Path(root)
    orbital_root = root / 'integration' / 'Orbital' / 'main'
    ensure_orbital_manifests(orbital_root)
    orbital_paths = ensure_orbital_report_dirs(orbital_root)

    orbital_run = run_global_pass(repo_root=orbital_root)
    final = dict(orbital_run.get('final', {}))
    state_manifest = build_state_manifest(final)
    health_manifest = build_health_manifest(final)
    recommended_control = recommend_control(final)
    sync_manifest = _build_sync_manifest(root)
    runtime_gating = _build_runtime_gating(sync_manifest)

    bridge_dir = root / BRIDGE_DIR
    bridge_dir.mkdir(parents=True, exist_ok=True)

    summary: dict[str, Any] = {
        'schema': 'ciel-sot-agent/orbital-bridge-report/v0.2',
        'source_report': str(Path('integration/Orbital/main/reports/global_orbital_coherence_pass/summary.json')),
        'source_paths': orbital_paths,
        'orbital_run': {'engine': orbital_run.get('engine'), 'steps': orbital_run.get('steps'), 'params': orbital_run.get('params', {})},
        'state_manifest': state_manifest,
        'health_manifest': health_manifest,
        'recommended_control': recommended_control,
        'subsystem_sync_manifest': sync_manifest,
        'runtime_gating': runtime_gating,
        'bridge_metrics': {
            'orbital_R_H': float(final.get('R_H', 0.0)),
            'orbital_closure_penalty': float(final.get('closure_penalty', 0.0)),
            'integration_closure_defect_proxy': max(0.0, min(1.0, 1.0 - float(final.get('R_H', 0.0)))),
            'topological_charge_global': float(final.get('Lambda_glob', 0.0)),
            'subsystem_board_count': int(sync_manifest.get('board_count', 0) or 0),
            'tau_system_count': int(sync_manifest.get('tau_system_count', 0) or 0),
        },
    }

    try:
        from .ciel_pipeline import run_ciel_pipeline
        ciel_result = run_ciel_pipeline(summary, context='orbital_bridge', root=root)
        summary['ciel_pipeline'] = {
            'status': ciel_result['ciel_status'],
            'dominant_emotion': ciel_result['dominant_emotion'],
            'mood': ciel_result['mood'],
            'soul_invariant': ciel_result['soul_invariant'],
            'ethical_score': ciel_result['ethical_score'],
            'orbital_context': ciel_result['orbital_context'],
        }
    except Exception as exc:
        _LOG.warning("CIEL/Ω pipeline unavailable: %s", exc)
        summary['ciel_pipeline'] = {'status': 'unavailable'}

    (bridge_dir / 'orbital_bridge_report.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    (bridge_dir / 'orbital_bridge_report.md').write_text(_bridge_markdown(summary), encoding='utf-8')
    (bridge_dir / 'orbital_state_manifest.json').write_text(json.dumps(state_manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    (bridge_dir / 'orbital_health_manifest.json').write_text(json.dumps(health_manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    (bridge_dir / 'subsystem_sync_manifest.json').write_text(json.dumps(sync_manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    (bridge_dir / 'runtime_gating.json').write_text(json.dumps(runtime_gating, ensure_ascii=False, indent=2), encoding='utf-8')
    return summary


def main() -> int:
    root = resolve_project_root(Path(__file__))
    summary = build_orbital_bridge(root)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
