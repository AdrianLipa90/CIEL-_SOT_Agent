# Orbital Bridge Report

## Source
- source_report: integration/Orbital/main/reports/global_orbital_coherence_pass/summary.json
- engine: global_orbital_coherence_pass_v63_euler_df257
- steps: 20

## State Manifest
- coherence_index: 0.930307813462336
- topological_charge_global: 0.06339365736030433
- phase_lock_error: 5.461642439862258
- beat_frequency_target_hz: 7.83
- spectral_radius_A: 1.4675652201527518
- fiedler_L: 0.023287741349184373
- zeta_enabled: True
- nonlocal_phi_ab_mean: 0.005517031549659778
- nonlocal_phi_berry_mean: -0.09813285682478182
- nonlocal_eba_defect_mean: 0.0474602150829184
- nonlocal_coherent_fraction: 1.0
- euler_bridge_closure_score: 0.5423376184759512
- euler_bridge_target_phase: 0.04456002892039556
- effective_rh: 0.12036051744392774
- timestamp: 2026-05-01T18:53:12.848564+00:00

## Health Manifest
- system_health: 0.5846115510810542
- risk_level: low
- closure_penalty: 5.461642439862258
- R_H: 0.030558029314220574
- T_glob: 1.7580808190776074
- Lambda_glob: 0.06339365736030433
- effective_rh: 0.12036051744392774
- rh_drivers: {'raw_rh': 0.030558029314220574, 'eba_defect': 0.0474602150829184, 'coherent_fraction': 1.0, 'closure_score': 0.5423376184759512, 'phase_gap': 0.045420556220784086}
- recommended_action: deep diagnostics allowed

## Recommended Control
- mode: standard
- phase_lock_enable: True
- target_phase_shift: 0.0006119151987408998
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
- rh_effective: 0.12036051744392774
- rh_drivers: {'raw_rh': 0.030558029314220574, 'eba_defect': 0.0474602150829184, 'coherent_fraction': 1.0, 'closure_score': 0.5423376184759512, 'phase_gap': 0.045420556220784086}
- notes: Stable but not deep-merge safe.

## Bridge Metrics
- orbital_R_H: 0.030558029314220574
- orbital_closure_penalty: 5.461642439862258
- integration_closure_defect_proxy: 0.9694419706857794
- topological_charge_global: 0.06339365736030433
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
- soul_invariant: 0.8625430101388623
- ethical_score: 0.6220563277587694
- orbital_context: orbital|mode=standard|R_H=0.0306|closure=5.4616|chirality=0.0634
- phi_ab_mean: 0.005517031549659778
- phi_berry_mean: -0.09813285682478182
- eba_defect_mean: 0.0474602150829184
- nonlocal_coherent_fraction: 1.0
- bridge_closure_score: 0.5423376184759512
- bridge_target_phase: 0.04456002892039556
- nonlocal_card_count: 5
- nonlocal_card_ids: ['NL-HOLOMEM-0001', 'NL-EBA-0002', 'NL-BRIDGE-0003', 'NL-PHASE-0004', 'NL-WIJ-0005']
- phase_R_H: 7.690738481277209e-05
- collatz_seed: 28
- lie4_trace: 4.183135222640001
- local_nonlocality_fallback: {'active': False, 'fallback_coherent_fraction': 1.0, 'merged_coherent_fraction': 1.0}