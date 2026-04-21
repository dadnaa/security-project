"""Event bus for in-process notifications."""

from __future__ import annotations

from typing import Callable, List


class EventBus:
    def __init__(self) -> None:
        self.subscribers: List[Callable[[dict], None]] = []

    def subscribe(self, fn: Callable[[dict], None]) -> None:
        self.subscribers.append(fn)

    def emit(self, event: dict) -> None:
        for fn in self.subscribers:
            fn(event)