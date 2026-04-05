# Global Orbital Coherence Pass

Read-only orbital coherence pass over the canonical repository structure.

- pass_label: orbital_orbital_mode=standard_R_H=0.8800_closure=0.0000_chirality=0.0000
- engine: global_orbital_coherence_pass_v64_runtime_bridge

## Initial
- R_H: 0.002299
- T_glob: 2.536566
- Lambda_glob: 0.000000
- closure_penalty: 5.997740
- V_rel_total: 6.380524
- radial_spread: 0.181309
- mean_spin: 0.000000
- spectral_radius_A: 1.379746
- spectral_gap_A: 0.614094
- fiedler_L: 0.237754
- zeta_enabled: True
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: 0.000000
- zeta_coupling_norm: 0.006802
- zeta_coupling_norm_raw: 0.855195
- zeta_spin: 0.000000
- zeta_rho: 0.450000
- D_f: 2.570000
- euler_leak_angle: 0.895354

## Final
- R_H: 0.021871
- T_glob: 2.403418
- Lambda_glob: 0.214500
- closure_penalty: 5.909336
- V_rel_total: 6.291720
- radial_spread: 0.182841
- mean_spin: -0.057893
- spectral_radius_A: 1.237970
- spectral_gap_A: 0.469350
- fiedler_L: 0.277292
- zeta_enabled: True
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: -0.000157
- zeta_coupling_norm: 0.006301
- zeta_coupling_norm_raw: 0.791106
- zeta_spin: -0.057893
- zeta_rho: 0.449902
- D_f: 2.570000
- euler_leak_angle: 0.895354

## Notes
- Geometry derived from imports + README mesh + AGENT mesh + manifests.
- The pass is read-only with respect to repository content; only reports/manifests are refreshed.
- Runtime policy is expected to consume R_H, closure_penalty, spectral observables, and zeta terms.