"""Scenario: simulate a rogue BTS attachment event."""  

from lab.core.network_state import NetworkStateManager


def run(manager: NetworkStateManager) -> dict:
    manager.log("scenario_start", "Rogue BTS scenario initiated")
    manager.update(tower="Rogue BTS", encryption="A5/1", signal="strong", notes="Rogue BTS simulated")
    manager.log("observation", "Device attaches to rogue BTS in simulation")
    manager.log("scenario_complete", "Rogue BTS scenario completed")
    return manager.snapshot()