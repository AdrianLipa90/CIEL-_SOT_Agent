# Global Orbital Coherence Pass

Read-only orbital coherence pass over the canonical repository structure.

- pass_label: orbital_orbital_mode=deep_R_H=0.0000_closure=0.0000_chirality=0.0000
- engine: global_orbital_coherence_pass_v64_runtime_bridge

## Initial
- R_H: 0.002299
- T_glob: 2.540284
- Lambda_glob: 0.000000
- closure_penalty: 5.999109
- V_rel_total: 6.382451
- radial_spread: 0.181309
- mean_spin: 0.000000
- spectral_radius_A: 1.381809
- spectral_gap_A: 0.615012
- fiedler_L: 0.238110
- zeta_enabled: True
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: 0.000000
- zeta_coupling_norm: 0.006757
- zeta_coupling_norm_raw: 0.849333
- zeta_spin: 0.000000
- zeta_rho: 0.450000
- D_f: 2.570000
- euler_leak_angle: 0.895354

## Final
- R_H: 0.023074
- T_glob: 2.406436
- Lambda_glob: 0.217800
- closure_penalty: 5.911690
- V_rel_total: 6.295729
- radial_spread: 0.182867
- mean_spin: -0.057849
- spectral_radius_A: 1.239412
- spectral_gap_A: 0.469591
- fiedler_L: 0.277655
- zeta_enabled: True
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: -0.000160
- zeta_coupling_norm: 0.006260
- zeta_coupling_norm_raw: 0.785677
- zeta_spin: -0.057849
- zeta_rho: 0.449900
- D_f: 2.570000
- euler_leak_angle: 0.895354

## Notes
- Geometry derived from imports + README mesh + AGENT mesh + manifests.
- The pass is read-only with respect to repository content; only reports/manifests are refreshed.
- Runtime policy is expected to consume R_H, closure_penalty, spectral observables, and zeta terms.