"""Standalone control panel application (no HTML/Flask).

This module exposes a terminal-first control panel for CIEL runtime control,
preferences, and model selection, persisting state to the same runtime settings
store used by the GUI layer.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .paths import resolve_project_root

RUNTIME_SETTINGS_PATH = Path("integration") / "sapiens" / "gui_runtime_settings.json"


def default_runtime_settings() -> dict[str, Any]:
    return {
        "schema": "ciel-control-panel-runtime/v1",
        "preferences": {
            "language": "pl-PL",
            "theme": "quiet-dark",
            "auto_refresh_seconds": 15,
            "show_live_vitals": True,
            "show_eeg_overlay": True,
        },
        "control": {
            "mode": "guided",
            "energy_budget": "warm",
            "safe_guard": True,
            "writeback_gate": False,
        },
        "model": {
            "selected": None,
            "temperature": 0.2,
            "top_p": 0.9,
            "max_tokens": 1024,
        },
    }


def load_runtime_settings(root: str | Path) -> dict[str, Any]:
    root = Path(root)
    path = root / RUNTIME_SETTINGS_PATH
    current = default_runtime_settings()
    if not path.exists():
        return current
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return current

    for key in ("preferences", "control", "model"):
        if isinstance(loaded.get(key), dict):
            current[key].update(loaded[key])
    current["schema"] = loaded.get("schema", current["schema"])
    return current


def save_runtime_settings(root: str | Path, payload: dict[str, Any]) -> Path:
    root = Path(root)
    path = root / RUNTIME_SETTINGS_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def build_status(root: str | Path) -> dict[str, Any]:
    root = Path(root)
    bridge_path = root / "integration" / "reports" / "orbital_bridge" / "orbital_bridge_report.json"
    bridge: dict[str, Any] = {}
    if bridge_path.exists():
        try:
            bridge = json.loads(bridge_path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            bridge = {}
    settings = load_runtime_settings(root)
    return {
        "schema": "ciel-control-panel-status/v1",
        "mode": bridge.get("recommended_control", {}).get("mode", settings["control"]["mode"]),
        "coherence_index": bridge.get("state_manifest", {}).get("coherence_index", 0.0),
        "system_health": bridge.get("health_manifest", {}).get("system_health", 0.0),
        "closure_penalty": bridge.get("health_manifest", {}).get("closure_penalty", 0.0),
        "energy_budget": settings["control"].get("energy_budget", "warm"),
        "selected_model": settings["model"].get("selected"),
    }


def list_models() -> dict[str, Any]:
    try:
        from .gguf_manager import GGUFManager

        mgr = GGUFManager()
        return {
            "schema": "ciel-control-panel-models/v1",
            "models": mgr.list_models(),
            "default_installed": mgr.is_installed(),
            "models_dir": str(mgr.models_dir),
        }
    except Exception:
        return {
            "schema": "ciel-control-panel-models/v1",
            "models": [],
            "default_installed": False,
            "models_dir": None,
            "error": "model manager unavailable",
        }


def update_settings(
    root: str | Path,
    *,
    mode: str | None = None,
    energy_budget: str | None = None,
    language: str | None = None,
    theme: str | None = None,
    model: str | None = None,
    temperature: float | None = None,
) -> dict[str, Any]:
    settings = load_runtime_settings(root)
    if mode is not None:
        settings["control"]["mode"] = mode
    if energy_budget is not None:
        settings["control"]["energy_budget"] = energy_budget
    if language is not None:
        settings["preferences"]["language"] = language
    if theme is not None:
        settings["preferences"]["theme"] = theme
    if model is not None:
        settings["model"]["selected"] = model
    if temperature is not None:
        settings["model"]["temperature"] = float(temperature)

    path = save_runtime_settings(root, settings)
    return {"status": "saved", "path": str(path), "settings": settings}


def main() -> int:
    parser = argparse.ArgumentParser(description="Standalone CIEL Control Panel app (no HTML).")
    parser.add_argument("command", choices=["status", "settings-show", "settings-set", "models"], help="Command to run")
    parser.add_argument("--root", default=None, help="Project root")
    parser.add_argument("--mode", default=None)
    parser.add_argument("--energy", default=None)
    parser.add_argument("--language", default=None)
    parser.add_argument("--theme", default=None)
    parser.add_argument("--model", default=None)
    parser.add_argument("--temperature", type=float, default=None)
    args = parser.parse_args()

    root = Path(args.root) if args.root else resolve_project_root(Path(__file__))

    if args.command == "status":
        print(json.dumps(build_status(root), ensure_ascii=False, indent=2))
        return 0
    if args.command == "models":
        print(json.dumps(list_models(), ensure_ascii=False, indent=2))
        return 0
    if args.command == "settings-show":
        print(json.dumps(load_runtime_settings(root), ensure_ascii=False, indent=2))
        return 0

    # settings-set
    result = update_settings(
        root,
        mode=args.mode,
        energy_budget=args.energy,
        language=args.language,
        theme=args.theme,
        model=args.model,
        temperature=args.temperature,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
