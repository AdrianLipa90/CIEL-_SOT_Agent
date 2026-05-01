# htri_daemon.py — src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/htri/htri_daemon.py

## Identity
- **path:** `src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/htri/htri_daemon.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** —
- **functions:** _handle_signal, _write_state, run_daemon, read_state, is_running

## Docstring
HTRI Daemon — trwały background process na i7-8750H + GTX 1050 Ti.

Działa non-stop, zapisuje metryki do ~/.claude/ciel_state.db co cycle_interval sekund.
Uruchamiany przez systemd lub autostart.

Usage:
    python3 htri_daemon.py          # foreground (do testów)
    python3 htri_daemon.py --daemon
