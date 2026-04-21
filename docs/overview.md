# IMSI Catcher & Rogue BTS Training Lab

This project provides a simulated environment to explore telecom security concepts safely.

## Goals
- Demonstrate how downgrade and rogue base station events affect network state.
- Provide a safe, local-only training environment.
- Emphasize that no real interception is performed.

## Architecture
- `lab.core`: state models and event tracking
- `lab.scenarios`: scripted scenarios
- `lab.api`: Flask API + UI
- `lab.ui`: browser UI assets
