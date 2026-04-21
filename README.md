# IMSI Catcher & Rogue BTS Training Lab

A safe, simulated lab for exploring telecom security concepts such as downgrade and rogue base station scenarios. This project does **not** perform real interception.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
lab run downgrade
lab serve
```

## Structure
- `src/lab/core`: models and event log
- `src/lab/scenarios`: simulation scenarios
- `src/lab/api`: Flask API + UI
- `docs`: usage documentation

## Disclaimer
This project is for education and training only. Use responsibly and legally.
