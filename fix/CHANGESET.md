# Install/runtime bridge fix changeset

Apply the following deltas on top of `main`.

## 1. `pyproject.toml`
Replace:

```toml
[tool.setuptools]
package-dir = {"" = "src"}
include-package-data = true

[tool.setuptools.packages.find]
where = ["src"]
include = ["ciel_sot_agent*"]
```

With:

```toml
[tool.setuptools]
include-package-data = true

[tool.setuptools.packages.find]
where = [".", "src"]
include = ["ciel_sot_agent*", "integration*"]

[tool.setuptools.package-data]
"integration" = ["**/*"]
"integration.Orbital" = ["**/*"]
"integration.Orbital.main" = ["**/*"]
```

## 2. Add import and root resolver in these files
For each file below:
- add `from .paths import resolve_project_root`
- replace `root = Path(__file__).resolve().parents[2]`
- with `root = resolve_project_root(__file__)`

Files:
- `src/ciel_sot_agent/synchronize.py`
- `src/ciel_sot_agent/synchronize_v2.py`
- `src/ciel_sot_agent/orbital_bridge.py`
- `src/ciel_sot_agent/sapiens_client.py`
- `src/ciel_sot_agent/gh_coupling.py`
- `src/ciel_sot_agent/gh_coupling_v2.py`
- `src/ciel_sot_agent/runtime_evidence_ingest.py`
- `src/ciel_sot_agent/index_validator.py`
- `src/ciel_sot_agent/index_validator_v2.py`

## 3. Validation
Run:

```bash
pip install -e .
python -m pip wheel .
CIEL_SOT_ROOT=$PWD ciel-sot-sync
CIEL_SOT_ROOT=$PWD ciel-sot-orbital-bridge
CIEL_SOT_ROOT=$PWD ciel-sot-sapiens-client "test"
```
