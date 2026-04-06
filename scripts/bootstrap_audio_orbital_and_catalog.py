#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


def repo_relative(repo_root: Path, path: Path) -> str:
    """
    Return a repository-relative POSIX-style string for a path when possible.

    Parameters:
        repo_root (Path): Repository root used as the base for relativization.
        path (Path): Path to convert to a repository-relative string.

    Returns:
        str: The path relative to `repo_root` with forward slashes, or the original path string if relativization fails.
    """
    try:
        return str(path.resolve().relative_to(repo_root.resolve())).replace("\\", "/")
    except Exception:
        return str(path)


def maybe_parse_json(text: str) -> dict[str, Any] | list[Any] | None:
    """
    Try to parse a stdout/stderr text blob as JSON.

    Returns parsed JSON on success; otherwise returns ``None``.
    """
    if not text or not text.strip():
        return None
    try:
        return json.loads(text)
    except Exception:
        return None


def load_json_if_exists(path: Path) -> dict[str, Any] | list[Any] | None:
    """
    Load a JSON artifact from disk when present.

    Returns ``None`` when the file does not exist or the payload is not valid JSON.
    """
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def run_step(repo_root: Path, script_name: str, extra_args: list[str] | None = None) -> dict:
    """
    Run a script from the repository's scripts directory and collect its execution results.

    Parameters:
        repo_root (Path): Repository root used to locate the script at `scripts/<script_name>`.
        script_name (str): Filename of the script to execute.
        extra_args (list[str] | None): Additional command-line arguments to append to the script invocation.

    Returns:
        dict: A mapping with the following keys:
            - 'script' (str): The script name that was run.
            - 'returncode' (int): The process exit code.
            - 'stdout' (str): Captured standard output.
            - 'stderr' (str): Captured standard error.
            - 'summary_json' (dict | list | None): Parsed JSON payload from stdout when available.
            - 'ok' (bool): `true` if `returncode` is 0, `false` otherwise.
    """
    script_path = repo_root / 'scripts' / script_name
    cmd = [sys.executable, str(script_path), '--repo-root', str(repo_root)]
    if extra_args:
        cmd.extend(extra_args)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return {
        'script': script_name,
        'returncode': proc.returncode,
        'stdout': proc.stdout,
        'stderr': proc.stderr,
        'summary_json': maybe_parse_json(proc.stdout),
        'ok': proc.returncode == 0,
    }


def main() -> int:
    """
    Orchestrates a sequence of repository scripts to build and validate the audio-orbital definition catalog and writes a JSON summary report.

    Parses command-line arguments `--repo-root`, `--skip-download`, and `--roots`; runs a fixed sequence of helper scripts, aggregates their results and selected artifact paths (made repository-relative), writes the aggregated summary to integration/registries/definitions/audio_orbital_hook_report.json, and prints the same JSON to stdout.

    Returns:
        int: `0` if all steps succeeded, `1` otherwise.
    """
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo-root', default='.')
    ap.add_argument('--skip-download', action='store_true')
    ap.add_argument('--roots', nargs='*', default=['src', 'scripts', 'integration'])
    args = ap.parse_args()

    repo_root = Path(args.repo_root).resolve()
    steps = []

    bootstrap_args: list[str] = []
    if args.skip_download:
        bootstrap_args.append('--skip-download')
    steps.append(run_step(repo_root, 'bootstrap_audio_orbital_stack.py', bootstrap_args))

    roots_args = ['--roots', *args.roots] if args.roots else []
    steps.append(run_step(repo_root, 'build_orbital_definition_registry.py', roots_args))
    steps.append(run_step(repo_root, 'normalize_definition_registry.py'))
    steps.append(run_step(repo_root, 'resolve_orbital_semantics.py'))
    steps.append(run_step(repo_root, 'build_nonlocal_definition_edges.py'))
    steps.append(run_step(repo_root, 'build_definition_db_library.py'))
    steps.append(run_step(repo_root, 'run_audio_orbital_probe.py'))

    ok = all(step['ok'] for step in steps)

    artifacts = {
        'audio_state': repo_relative(repo_root, repo_root / 'integration' / 'imports' / 'audio_orbital_stack' / 'state' / 'audio_orbital_stack_state.json'),
        'definition_registry': repo_relative(repo_root, repo_root / 'integration' / 'registries' / 'definitions' / 'definition_registry.json'),
        'orbital_registry': repo_relative(repo_root, repo_root / 'integration' / 'registries' / 'definitions' / 'orbital_definition_registry.json'),
        'orbital_report': repo_relative(repo_root, repo_root / 'integration' / 'registries' / 'definitions' / 'orbital_assignment_report.json'),
        'nonlocal_edges': repo_relative(repo_root, repo_root / 'integration' / 'registries' / 'definitions' / 'nonlocal_definition_edges.json'),
        'db_manifest': repo_relative(repo_root, repo_root / 'integration' / 'registries' / 'definitions' / 'db_library' / 'manifest.json'),
    }

    artifact_snapshots = {
        'audio_state': load_json_if_exists(repo_root / artifacts['audio_state']),
        'orbital_report': load_json_if_exists(repo_root / artifacts['orbital_report']),
        'db_manifest': load_json_if_exists(repo_root / artifacts['db_manifest']),
    }

    summary = {
        'schema': 'ciel/audio-orbital-catalog-hook/v0.2',
        'ok': ok,
        'steps': steps,
        'artifacts': artifacts,
        'artifact_snapshots': artifact_snapshots,
    }

    out_path = repo_root / 'integration' / 'registries' / 'definitions' / 'audio_orbital_hook_report.json'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(json.dumps(summary, indent=2))
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
