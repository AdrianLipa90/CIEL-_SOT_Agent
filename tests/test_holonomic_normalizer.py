from __future__ import annotations

from types import SimpleNamespace

from src.ciel_sot_agent.holonomic_normalizer import (
    HolonomicCallbacks,
    circular_barycenter,
    circular_distance,
    clip_couplings,
    holonomic_system_normalizer_v2,
    renormalize_couplings,
    symmetrize_couplings,
    wrap,
)


def test_wrap_keeps_angle_in_principal_interval() -> None:
    value = wrap(4.0)
    assert -3.141592653589793 < value <= 3.141592653589793


def test_circular_helpers_return_expected_shapes() -> None:
    phi = circular_barycenter([0.0, 1.0], [0.5, 0.5])
    assert isinstance(phi, float)
    assert circular_distance(0.0, 0.0) == 0.0


def test_coupling_postprocessing_is_stable() -> None:
    couplings = {("a", "b"): 2.0, ("b", "a"): 0.0}
    sym = symmetrize_couplings(couplings)
    clipped = clip_couplings(sym, lo=0.0, hi=1.0)
    renorm = renormalize_couplings(clipped, target_norm="l1")
    assert renorm[("a", "b")] == renorm[("b", "a")]
    assert abs(sum(abs(v) for v in renorm.values()) - 1.0) < 1e-9


def _callbacks() -> HolonomicCallbacks:
    return HolonomicCallbacks(
        closure_defect=lambda repo_states: 0.05,
        all_pairwise_tensions=lambda repo_states, couplings: [{"tension": 0.1}],
        compute_placeholder_penalty=lambda objects: 0.0,
        compute_demo_legacy_penalty=lambda objects: 0.0,
        compute_semantic_execution_seam_penalty=lambda X: 0.01,
        object_break_penalty=lambda obj: 0.0,
        seam_local_penalty=lambda X, obj: 0.0,
        local_tension=lambda X, i, j: 0.1,
        recompute_manifests_and_bridge=lambda X: X,
    )


def _state() -> SimpleNamespace:
    return SimpleNamespace(
        repo_states={"canon": {"phase": 0.0}},
        couplings={("a", "b"): 0.5, ("b", "a"): 0.3},
        orbital_final={"closure_penalty": 5.0},
        sectors={
            "affect": SimpleNamespace(phi=1.0, amplitude=1.0, decoherence=0.1, min_amplitude_floor=0.05),
            "memory": SimpleNamespace(lobes=[0.8, 1.2], lobe_weights=[0.7, 0.3], decoherence=0.1),
            "core": SimpleNamespace(phi=0.0, decoherence=0.05),
            "vocabulary": SimpleNamespace(phi=0.4, decoherence=0.02),
        },
        distortion={"lie": 0.0, "omit": 0.0, "hallucinate": 0.0, "smooth": 0.0},
        objects=[SimpleNamespace(exec_weight=1.0)],
        quality={"a": 1.0, "b": 1.0},
        thresholds={"seam_ok": 0.15},
        max_coupling=1.0,
        mode="deep",
        allow_writeback=True,
    )


def test_holonomic_normalizer_returns_state_and_sets_objective() -> None:
    X = holonomic_system_normalizer_v2(_state(), _callbacks(), max_iter=2)
    assert hasattr(X, "J")
    assert X.mode in {"safe", "standard", "deep"}
    assert isinstance(X.couplings, dict)
