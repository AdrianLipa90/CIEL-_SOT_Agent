# Orbital Bridge Report

## Source
- source_report: integration/Orbital/main/reports/global_orbital_coherence_pass/summary.json
- engine: global_orbital_coherence_pass_v63_euler_df257
- steps: 20

## State Manifest
- coherence_index: 0.9444151494339608
- topological_charge_global: 0.14538611511321484
- phase_lock_error: 5.426625056924105
- beat_frequency_target_hz: 7.83
- spectral_radius_A: 1.7058158434883552
- fiedler_L: 0.027920098943528735
- zeta_enabled: True
- nonlocal_phi_ab_mean: 0.005994399033428393
- nonlocal_phi_berry_mean: -0.09836923932143869
- nonlocal_eba_defect_mean: 0.04786185672810459
- nonlocal_coherent_fraction: 1.0
- euler_bridge_closure_score: 0.5423376184759512
- euler_bridge_target_phase: 0.04456002892039556
- effective_rh: 0.09474937591120768
- timestamp: 2026-05-01T15:24:12.385724+00:00

## Health Manifest
- system_health: 0.5956283664616303
- risk_level: low
- closure_penalty: 5.426625056924105
- R_H: 0.004798788917124673
- T_glob: 2.1109684303419707
- Lambda_glob: 0.14538611511321484
- effective_rh: 0.09474937591120768
- rh_drivers: {'raw_rh': 0.004798788917124673, 'eba_defect': 0.04786185672810459, 'coherent_fraction': 1.0, 'closure_score': 0.5423376184759512, 'phase_gap': 0.04549579910639072}
- recommended_action: deep diagnostics allowed

## Recommended Control
- mode: standard
- phase_lock_enable: True
- target_phase_shift: 0.011509543251112815
- target_phase_memory: 0.04456002892039556
- dt_override: 0.0205
- zeta_coupling_scale: 0.35
- mu_phi: 0.18
- epsilon_hom: 0.22
- nonlocal_gate: True
- euler_memory_lock: True
- writeback_gate: True
- rh_mode: normal_operation
- rh_severity: low
- rh_effective: 0.09474937591120768
- rh_drivers: {'raw_rh': 0.004798788917124673, 'eba_defect': 0.04786185672810459, 'coherent_fraction': 1.0, 'closure_score': 0.5423376184759512, 'phase_gap': 0.04549579910639072}
- notes: Stable but not deep-merge safe.

## Bridge Metrics
- orbital_R_H: 0.004798788917124673
- orbital_closure_penalty: 5.426625056924105
- integration_closure_defect_proxy: 0.9952012110828753
- topological_charge_global: 0.14538611511321484
- subsystem_board_count: 763
- tau_system_count: 1
- nonlocal_card_count: 5

## Subsystem Sync Manifest
- board_count: 763
- avg_members_per_board: 5.071
- tau_orbit_count: 763
- tau_system_count: 1
- nonlocal_card_count: 5
- nonlocal_card_classes: nonlocal_memory_orchestrator, nonlocal_phase_memory_card_set, nonlocal_reduction_bridge, orbital_coupling_optimizer, phase_dynamics_runtime

## Runtime Gating
- dominant_privacy_constraint: GRADIENT_LIMITED_DISCLOSURE
- dominant_horizon_class: POROUS
- export_boundary_mode: PROJECTED_ONLY
- private_state_export_allowed: False
- board_sync_ready: True
- system_tau_coherent: True
- requires_projection_operator: True

## CIEL Pipeline
- status: ok
- dominant_emotion: love
- mood: 0.8866971661245503
- soul_invariant: 0.9398588095014286
- ethical_score: 0.6220563277587694
- orbital_context: orbital|mode=standard|R_H=0.0048|closure=5.4266|chirality=0.1454
- phi_ab_mean: 0.005994399033428393
- phi_berry_mean: -0.09836923932143869
- eba_defect_mean: 0.04786185672810459
- nonlocal_coherent_fraction: 1.0
- bridge_closure_score: 0.5423376184759512
- bridge_target_phase: 0.04456002892039556
- nonlocal_card_count: 5
- nonlocal_card_ids: ['NL-HOLOMEM-0001', 'NL-EBA-0002', 'NL-BRIDGE-0003', 'NL-PHASE-0004', 'NL-WIJ-0005']
- phase_R_H: 7.690738481277209e-05
- collatz_seed: 28
- lie4_trace: 4.183135222640001
- local_nonlocality_fallback: {'active': False, 'fallback_coherent_fraction': 1.0, 'merged_coherent_fraction': 1.0}