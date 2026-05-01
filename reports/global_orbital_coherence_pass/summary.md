# Global Orbital Coherence Pass

Read-only diagnostic pass over the canonical repository structure.

## Initial
- R_H: 0.038719
- T_glob: 1.245470
- Lambda_glob: 0.000000
- closure_penalty: 5.959041
- V_rel_total: 6.184581
- radial_spread: 0.181309
- mean_spin: 0.000000
- spectral_radius_A: 1.119721
- spectral_gap_A: 0.101845
- fiedler_L: 0.079943
- zeta_enabled: True
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: 0.000000
- zeta_coupling_norm: 0.006178
- zeta_coupling_norm_raw: 0.776913
- zeta_spin: 0.000000
- zeta_rho: 0.450000
- D_f: 2.570000
- euler_leak_angle: 0.895354

## Final
- R_H: 0.043652
- T_glob: 1.610090
- Lambda_glob: 0.000611
- closure_penalty: 6.236807
- V_rel_total: 6.521972
- radial_spread: 0.198171
- mean_spin: 0.078753
- spectral_radius_A: 0.856928
- spectral_gap_A: 0.025046
- fiedler_L: 0.255392
- zeta_enabled: True
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: 0.002012
- zeta_coupling_norm: 0.005173
- zeta_coupling_norm_raw: 0.650363
- zeta_spin: 0.078753
- zeta_rho: 0.451280
- D_f: 2.570000
- euler_leak_angle: 0.895354

## Notes
- Geometry derived from imports + README mesh + AGENT mesh + manifests.
- v6.3 uses Euler-rotated homology leak with D_f-dependent radial/angular split.
- berry_phase written back to sectors_global.json after each pass for holonomy continuity.