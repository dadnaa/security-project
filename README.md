# security-project

A small Python simulation of a rogue base station (Rogue BTS) attack flow and basic defensive detection.

The project models:
- **Attack path**: rogue BTS attraction, forced network downgrade to 2G, and IMSI capture.
- **Defense path**: simple detection rules, alert generation, and CTF-style flags.
- **Dashboard**: a Flask UI/API to trigger the attack and view live state.

## Project structure

```text
attack/     Attack simulation modules + attack flow script
core/       Shared network state and event primitives
defense/    Detection, alerting, and flag evaluation
dashboard/  Flask dashboard and API
```

## Requirements

- Python 3.10+ (tested here with Python 3.14)
- `flask` (required for `dashboard/app.py`)

There is currently no `requirements.txt` or `pyproject.toml` in this repository.

## Setup

From the repository root:

```bash
python -m pip install --upgrade pip
python -m pip install flask
```

## Running the project

Run these commands from the repository root using module mode (`python -m ...`):

```bash
python -m attack.test_attack
python -m defense.test_defense
python -m core.test_core
```

Start the dashboard:

```bash
python -m dashboard.app
```

Then open: `http://127.0.0.1:5000`

Available endpoints:
- `GET /` — dashboard UI
- `GET /attack` — starts attack sequence in a background thread
- `GET /status` — current network, alert, and flag state

## Testing

This repository does not currently include a formal test framework (e.g., `pytest`).
The scripts in `attack/test_attack.py`, `defense/test_defense.py`, and `core/test_core.py` serve as runnable simulation checks.

## Security notes and limitations

- This is an educational simulation, not a production telecom security system.
- Detection logic is intentionally rule-based and simplified.
- IMSI values are randomly generated mock values.
- The dashboard runs with `debug=True` in `dashboard/app.py`; avoid using that setting in production-like environments.

## Contributing

Contributions are welcome. Keep changes focused, preserve module-based run commands, and update this README when behavior or setup changes.
