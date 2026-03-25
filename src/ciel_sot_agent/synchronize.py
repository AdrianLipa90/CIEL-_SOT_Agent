from __future__ import annotations

import json
from pathlib import Path

from .repo_phase import build_sync_report


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    registry_path = root / 'integration' / 'repository_registry.json'
    couplings_path = root / 'integration' / 'couplings.json'
    report = build_sync_report(registry_path, couplings_path)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
