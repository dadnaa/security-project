"""Network state container used by scenarios and UI."""

from __future__ import annotations

from typing import Dict, List

from lab.core.config import DEFAULT_STATE
from lab.core.models import NetworkState, LabEvent
from lab.core.events import EventBus


class NetworkStateManager:
    def __init__(self) -> None:
        self.state = NetworkState(**DEFAULT_STATE)
        self.events: List[LabEvent] = []
        self.bus = EventBus()

    def update(self, **kwargs) -> NetworkState:
        for key, value in kwargs.items():
            setattr(self.state, key, value)
        event = LabEvent.create("state_updated", f"State updated: {kwargs}")
        self.events.append(event)
        self.bus.emit(event.to_dict())
        return self.state

    def log(self, name: str, detail: str) -> None:
        event = LabEvent.create(name, detail)
        self.events.append(event)
        self.bus.emit(event.to_dict())

    def snapshot(self) -> Dict:
        return self.state.to_dict()

    def event_log(self) -> List[Dict]:
        return [event.to_dict() for event in self.events]