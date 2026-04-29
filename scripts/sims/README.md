# CIEL Simulations & Benchmarks

Simulation and benchmark scripts directory.
Preserved between sessions to avoid re-running.

| Script | Description | Latest results |
|---|---|---|
| `energy_benchmark.py` | CIEL energy consumption vs Claude API | M0-M8: ~98mJ/step, pipeline: ~23J, Claude server: ~5040J/call |
| `htri_mini.py` *(symlink → ../htri_mini.py)* | Kuramoto 768 oscillators on CPU/GPU | — (not run on GPU) |

## Convention

- Each script contains a docstring with description, parameters, and latest results.
- Record results in the docstring on each run with the date.
- Do not remove scripts without reason — even "one-off" scripts may be useful later.
