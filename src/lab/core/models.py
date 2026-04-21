"""Data models for lab state and events."""

from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict


@dataclass
class NetworkState:
    tower: str
    encryption: str
    signal: str
    imsi_exposed: bool
    notes: str

    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass
class LabEvent:
    name: str
    detail: str
    timestamp: str

    @classmethod
    def create(cls, name: str, detail: str) -> "LabEvent":
        return cls(name=name, detail=detail, timestamp=datetime.utcnow().isoformat() + "Z")

    def to_dict(self) -> Dict:
        return asdict(self)