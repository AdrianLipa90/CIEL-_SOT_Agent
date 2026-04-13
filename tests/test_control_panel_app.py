from __future__ import annotations

import json
from pathlib import Path

from src.ciel_sot_agent.control_panel_app import (
    RUNTIME_SETTINGS_PATH,
    build_status,
    default_runtime_settings,
    load_runtime_settings,
    save_runtime_settings,
    update_settings,
)


def test_default_runtime_settings_contains_sections() -> None:
    data = default_runtime_settings()
    assert data["schema"] == "ciel-control-panel-runtime/v1"
    assert "preferences" in data
    assert "control" in data
    assert "model" in data


def test_load_runtime_settings_returns_defaults_when_missing(tmp_path: Path) -> None:
    loaded = load_runtime_settings(tmp_path)
    assert loaded["schema"] == "ciel-control-panel-runtime/v1"
    assert loaded["control"]["mode"] == "guided"


def test_save_and_load_runtime_settings_roundtrip(tmp_path: Path) -> None:
    payload = default_runtime_settings()
    payload["control"]["mode"] = "safe"
    path = save_runtime_settings(tmp_path, payload)
    assert path == tmp_path / RUNTIME_SETTINGS_PATH

    loaded = load_runtime_settings(tmp_path)
    assert loaded["control"]["mode"] == "safe"


def test_update_settings_persists_selected_values(tmp_path: Path) -> None:
    out = update_settings(
        tmp_path,
        mode="diagnostic",
        energy_budget="performance",
        language="en-US",
        theme="high-contrast",
        model="demo.gguf",
        temperature=0.55,
    )
    assert out["status"] == "saved"

    loaded = json.loads((tmp_path / RUNTIME_SETTINGS_PATH).read_text(encoding="utf-8"))
    assert loaded["control"]["mode"] == "diagnostic"
    assert loaded["control"]["energy_budget"] == "performance"
    assert loaded["preferences"]["language"] == "en-US"
    assert loaded["preferences"]["theme"] == "high-contrast"
    assert loaded["model"]["selected"] == "demo.gguf"
    assert loaded["model"]["temperature"] == 0.55


def test_build_status_uses_bridge_when_available(tmp_path: Path) -> None:
    bridge_dir = tmp_path / "integration" / "reports" / "orbital_bridge"
    bridge_dir.mkdir(parents=True)
    report = {
        "recommended_control": {"mode": "safe"},
        "state_manifest": {"coherence_index": 0.81},
        "health_manifest": {"system_health": 0.73, "closure_penalty": 0.22},
    }
    (bridge_dir / "orbital_bridge_report.json").write_text(json.dumps(report), encoding="utf-8")

    status = build_status(tmp_path)
    assert status["schema"] == "ciel-control-panel-status/v1"
    assert status["mode"] == "safe"
    assert status["coherence_index"] == 0.81
    assert status["system_health"] == 0.73
    assert status["closure_penalty"] == 0.22
