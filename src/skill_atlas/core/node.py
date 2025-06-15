from __future__ import annotations

from attrs import define, field
from typing import Any


def _payload_factory() -> dict[str, Any]:
    return {}


@define(frozen=True, slots=True)
class Node:
    """Immutable graph node."""

    id: str
    name: str
    description: str
    icon_path: str | None = None
    payload: dict[str, Any] = field(factory=_payload_factory, hash=False)


@define(frozen=True, slots=True)
class Edge:
    """Connection between two nodes."""

    head: str
    tail: str
    directed: bool = False
    payload: dict[str, Any] = field(factory=_payload_factory, hash=False)
