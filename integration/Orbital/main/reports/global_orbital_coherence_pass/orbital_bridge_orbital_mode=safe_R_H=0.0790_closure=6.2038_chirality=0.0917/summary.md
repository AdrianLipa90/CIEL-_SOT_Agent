# Global Orbital Coherence Pass

Read-only orbital coherence pass over the canonical repository structure.

- pass_label: orbital_bridge_orbital_mode=safe_R_H=0.0790_closure=6.2038_chirality=0.0917
- engine: global_orbital_coherence_pass_v64_runtime_bridge

## Initial
- R_H: 0.002299
- T_glob: 2.479486
- Lambda_glob: 0.000000
- closure_penalty: 5.977317
- V_rel_total: 6.351539
- radial_spread: 0.181309
- mean_spin: 0.000000
- spectral_radius_A: 1.348463
- spectral_gap_A: 0.600170
- fiedler_L: 0.232364
- zeta_enabled: True
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: 0.000000
- zeta_coupling_norm: 0.006977
- zeta_coupling_norm_raw: 0.878032
- zeta_spin: 0.000000
- zeta_rho: 0.450000
- D_f: 2.570000
- euler_leak_angle: 0.895354

## Final
- R_H: 0.013334
- T_glob: 2.356746
- Lambda_glob: 0.192346
- closure_penalty: 5.883481
- V_rel_total: 6.250327
- radial_spread: 0.182697
- mean_spin: -0.054386
- spectral_radius_A: 1.215568
- spectral_gap_A: 0.464443
- fiedler_L: 0.271517
- zeta_enabled: True
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: -0.000141
- zeta_coupling_norm: 0.006466
- zeta_coupling_norm_raw: 0.812571
- zeta_spin: -0.054386
- zeta_rho: 0.449912
- D_f: 2.570000
- euler_leak_angle: 0.895354

## Notes
- Geometry derived from imports + README mesh + AGENT mesh + manifests.
- The pass is read-only with respect to repository content; only reports/manifests are refreshed.
- Runtime policy is expected to consume R_H, closure_penalty, spectral observables, and zeta terms.