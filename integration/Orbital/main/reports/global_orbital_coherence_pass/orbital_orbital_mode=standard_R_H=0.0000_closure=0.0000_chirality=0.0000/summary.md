# Global Orbital Coherence Pass

Read-only orbital coherence pass over the canonical repository structure.

- pass_label: orbital_orbital_mode=standard_R_H=0.0000_closure=0.0000_chirality=0.0000
- engine: global_orbital_coherence_pass_v64_runtime_bridge

## Initial
- R_H: 0.002299
- T_glob: 2.504952
- Lambda_glob: 0.000000
- closure_penalty: 5.986308
- V_rel_total: 6.364351
- radial_spread: 0.181309
- mean_spin: 0.000000
- spectral_radius_A: 1.362407
- spectral_gap_A: 0.606377
- fiedler_L: 0.234767
- zeta_enabled: True
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: 0.000000
- zeta_coupling_norm: 0.006916
- zeta_coupling_norm_raw: 0.870118
- zeta_spin: 0.000000
- zeta_rho: 0.450000
- D_f: 2.570000
- euler_leak_angle: 0.895354

## Final
- R_H: 0.016549
- T_glob: 2.377618
- Lambda_glob: 0.200919
- closure_penalty: 5.894472
- V_rel_total: 6.267664
- radial_spread: 0.182752
- mean_spin: -0.056389
- spectral_radius_A: 1.225612
- spectral_gap_A: 0.466721
- fiedler_L: 0.274113
- zeta_enabled: True
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: -0.000148
- zeta_coupling_norm: 0.006409
- zeta_coupling_norm_raw: 0.805092
- zeta_spin: -0.056389
- zeta_rho: 0.449907
- D_f: 2.570000
- euler_leak_angle: 0.895354

## Notes
- Geometry derived from imports + README mesh + AGENT mesh + manifests.
- The pass is read-only with respect to repository content; only reports/manifests are refreshed.
- Runtime policy is expected to consume R_H, closure_penalty, spectral observables, and zeta terms.