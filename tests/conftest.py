import sys
from pathlib import Path

_src = Path(__file__).parent.parent / "src"
for _p in [str(_src), str(_src / "CIEL_OMEGA_COMPLETE_SYSTEM"), str(_src / "CIEL_OMEGA_COMPLETE_SYSTEM" / "ciel_omega")]:
    if _p not in sys.path:
        sys.path.insert(0, _p)
