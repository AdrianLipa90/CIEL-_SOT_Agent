# Global Orbital Coherence Pass

Read-only diagnostic pass over the canonical repository structure.

## Initial
- R_H: 0.012863
- T_glob: 2.006886
- Lambda_glob: 0.000000
- closure_penalty: 5.492827
- V_rel_total: 5.806722
- radial_spread: 0.181309
- mean_spin: 0.000000
- spectral_radius_A: 1.405223
- spectral_gap_A: 0.009758
- fiedler_L: 0.025692
- zeta_enabled: True
- orbital_law_v0_enabled: False
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: 0.000000
- zeta_coupling_norm: 0.007300
- zeta_coupling_norm_raw: 0.920782
- zeta_spin: 0.000000
- zeta_rho: 0.450000
- D_f: 2.570000
- euler_leak_angle: 0.895354
- nonlocal_observables_present: True
- nonlocal_phi_ab_mean: 0.005685
- nonlocal_phi_berry_mean: -0.098220
- nonlocal_eba_defect_mean: 0.047595
- nonlocal_coherent_fraction: 1.000000
- euler_bridge_closure_score: 0.542338
- euler_bridge_target_phase: 0.044560

## Final
- R_H: 0.004799
- T_glob: 2.110968
- Lambda_glob: 0.145386
- closure_penalty: 5.426625
- V_rel_total: 5.748069
- radial_spread: 0.191374
- mean_spin: 0.000420
- spectral_radius_A: 1.705816
- spectral_gap_A: 0.739099
- fiedler_L: 0.027920
- zeta_enabled: True
- orbital_law_v0_enabled: False
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: -0.000370
- zeta_coupling_norm: 0.005954
- zeta_coupling_norm_raw: 0.751058
- zeta_spin: 0.000420
- zeta_rho: 0.449763
- D_f: 2.570000
- euler_leak_angle: 0.895354
- nonlocal_observables_present: True
- nonlocal_phi_ab_mean: 0.005685
- nonlocal_phi_berry_mean: -0.098220
- nonlocal_eba_defect_mean: 0.047595
- nonlocal_coherent_fraction: 1.000000
- euler_bridge_closure_score: 0.542338
- euler_bridge_target_phase: 0.044560

## Nonlocal Cards
- registry_present: True
- card_count: 5
- active_statuses: ACTIVE_CANONICAL_COUPLING_OPTIMIZER, ACTIVE_CANONICAL_NONLOCAL_BRIDGE, ACTIVE_CANONICAL_NONLOCAL_CARD_SET, ACTIVE_CANONICAL_NONLOCAL_RUNTIME, ACTIVE_CANONICAL_PHASE_RUNTIME
- eba_ready: True
- phase_ready: True
- bridge_ready: True

## Nonlocal / Euler Observables
- nonlocal_observables_present: True
- nonlocal_phi_ab_mean: 0.005685
- nonlocal_phi_berry_mean: -0.098220
- nonlocal_eba_defect_mean: 0.047595
- nonlocal_coherent_fraction: 1.000000
- euler_bridge_closure_score: 0.542338
- euler_bridge_target_phase: 0.044560

## Notes
- Geometry derived from imports + README mesh + AGENT mesh + manifests.
- v6.3 uses Euler-rotated homology leak with D_f-dependent radial/angular split.
- When enabled, Orbital Law v0 adds effective attractor strength, orbital period, winding, and phase-slip tracking.
- This pass is diagnostic only; it does not mutate repo content.