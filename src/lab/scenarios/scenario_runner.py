"""Scenario runner for the training lab."""

from __future__ import annotations

from typing import Dict, Callable

from lab.core.network_state import NetworkStateManager
from lab.scenarios import downgrade, rogue_bts, imsi_catcher


class ScenarioRunner:
    def __init__(self) -> None:
        self.manager = NetworkStateManager()

    @staticmethod
    def available_scenarios() -> list:
        return ["downgrade", "rogue_bts", "imsi_catcher"]

    def run(self, scenario: str) -> Dict:
        scenarios: Dict[str, Callable] = {
            "downgrade": downgrade.run,
            "rogue_bts": rogue_bts.run,
            "imsi_catcher": imsi_catcher.run,
        }
        if scenario not in scenarios:
            raise ValueError(f"Unknown scenario: {scenario}")
        return scenarios[scenario](self.manager)

    def status(self) -> Dict:
        return self.manager.snapshot()

    def logs(self) -> Dict:
        return {"events": self.manager.event_log()}