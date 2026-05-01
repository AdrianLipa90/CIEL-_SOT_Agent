#!/usr/bin/env python3
"""HTRI Mini — dense matrix Kuramoto on 768 oscillators.

This version removes the hand-built adjacency loops and uses the shared
vectorized phase-network core. The model is still classical: matrix coupling,
potential energy, and a winding-number trace.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src" / "CIEL_OMEGA_COMPLETE_SYSTEM"))

from ciel_omega.htri.htri_matrix import DensePhaseNetwork

N = 768
GRID_W = 32
GRID_H = 24
DT = 0.01
N_STEPS = 5000
RECORD_EVERY = 50
OMEGA_0_HZ = 7.83
KAPPA = 0.16

print(f"HTRI Mini — {N} oscillators on a dense phase matrix")
print(f"ω₀ = {OMEGA_0_HZ:.2f} Hz (Schumann target, diagnostic only)")
print(f"Kappa = {KAPPA:.3f}, grid = {GRID_W}×{GRID_H}, dt = {DT}")
print()

network = DensePhaseNetwork(
    n=N,
    dt=DT,
    kappa=KAPPA,
    topology="grid_2d",
    grid_shape=(GRID_W, GRID_H),
    field_strength=0.015,
)

history_r: list[float] = []
history_t: list[float] = []
history_potential: list[float] = []

print("Running dense Kuramoto + potential + winding trace...")
t_start = time.time()
for step in range(N_STEPS):
    network.step()
    if step % RECORD_EVERY == 0:
        snap = network.snapshot()
        history_r.append(float(snap["coherence"]))
        history_t.append(step * DT)
        history_potential.append(float(snap["potential"]))
        if step % 2000 == 0:
            print(
                f"  t={step*DT:6.1f}s | r={snap['coherence']:.4f} | "
                f"V={snap['potential']:.4f} | Σ={snap['soul_invariant']:.2f}"
            )

t_sim = time.time() - t_start
snap = network.snapshot()

ohm = np.unwrap(np.angle(np.exp(1j * network.phases)))
if len(history_r) > 10:
    r_mean = float(np.mean(history_r[len(history_r)//2:]))
else:
    r_mean = float(snap["coherence"])

print()
print("=" * 60)
print("  HTRI MINI — RESULTS")
print("=" * 60)
print(f"  Order parameter r:   {snap['coherence']:.4f}")
print(f"  r (post-transient):  {r_mean:.4f}")
print(f"  Potential energy:    {snap['potential']:.6f}")
print(f"  Soul invariant mean: {snap['soul_invariant']:.2f}")
print(f"  Spectral radius:     {snap['spectral_radius']:.4f}")
print(f"  Field norm:          {snap['field_norm']:.4f}")
print(f"  Sim time:            {N_STEPS*DT:.1f}s ({t_sim:.2f}s real)")
print("=" * 60)

out = Path(__file__).parent.parent / "integration" / "reports" / "htri_mini_result.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps({
    "n": N,
    "grid": [GRID_W, GRID_H],
    "steps": N_STEPS,
    "dt": DT,
    "kappa": KAPPA,
    "final": snap,
    "history_r": history_r,
    "history_t": history_t,
    "history_potential": history_potential,
}, indent=2), encoding="utf-8")
print(f"\n  Results saved: {out}")

if __name__ == "__main__":
    pass
