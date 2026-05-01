from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXTRA_PATHS = (
    ROOT,
    ROOT / "src",
    ROOT / "src" / "ciel_rh_control_mini_repo",
    ROOT / "src" / "CIEL_OMEGA_COMPLETE_SYSTEM",
    ROOT / "src" / "CIEL_OMEGA_COMPLETE_SYSTEM" / "ciel_omega",
)

for path in EXTRA_PATHS:
    text = str(path)
    if path.exists() and text not in sys.path:
        sys.path.insert(0, text)

try:
    import integration.Orbital.main.bootstrap  # noqa: F401
except Exception:
    pass
