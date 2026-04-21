"""Scenario: simulate IMSI collection exposure event."""  

from lab.core.network_state import NetworkStateManager


def run(manager: NetworkStateManager) -> dict:
    manager.log("scenario_start", "IMSI catcher scenario initiated")
    manager.update(imsi_exposed=True, notes="IMSI exposure simulated")
    manager.log("observation", "IMSI visibility simulated for training")
    manager.log("scenario_complete", "IMSI catcher scenario completed")
    return manager.snapshot()