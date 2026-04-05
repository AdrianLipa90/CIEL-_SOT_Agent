# Global Orbital Coherence Pass

Read-only orbital coherence pass over the canonical repository structure.

- pass_label: orbital_orbital_mode=safe_R_H=0.0790_closure=6.2038_chirality=0.0917
- engine: global_orbital_coherence_pass_v64_runtime_bridge

## Initial
- R_H: 0.002299
- T_glob: 2.471570
- Lambda_glob: 0.000000
- closure_penalty: 5.974559
- V_rel_total: 6.347593
- radial_spread: 0.181309
- mean_spin: 0.000000
- spectral_radius_A: 1.344121
- spectral_gap_A: 0.598238
- fiedler_L: 0.231616
- zeta_enabled: True
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: 0.000000
- zeta_coupling_norm: 0.007005
- zeta_coupling_norm_raw: 0.881771
- zeta_spin: 0.000000
- zeta_rho: 0.450000
- D_f: 2.570000
- euler_leak_angle: 0.895354

## Final
- R_H: 0.012330
- T_glob: 2.350248
- Lambda_glob: 0.189411
- closure_penalty: 5.879993
- V_rel_total: 6.244860
- radial_spread: 0.182676
- mean_spin: -0.053610
- spectral_radius_A: 1.212430
- spectral_gap_A: 0.463731
- fiedler_L: 0.270707
- zeta_enabled: True
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: -0.000139
- zeta_coupling_norm: 0.006493
- zeta_coupling_norm_raw: 0.816074
- zeta_spin: -0.053610
- zeta_rho: 0.449913
- D_f: 2.570000
- euler_leak_angle: 0.895354

## Notes
- Geometry derived from imports + README mesh + AGENT mesh + manifests.
- The pass is read-only with respect to repository content; only reports/manifests are refreshed.
- Runtime policy is expected to consume R_H, closure_penalty, spectral observables, and zeta terms.