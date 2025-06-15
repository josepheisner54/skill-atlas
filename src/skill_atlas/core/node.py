from __future__ import annotations

from attrs import define, field
from typing import Any, Set


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

    # ------------------------------------------------------------------
    def is_abstract(self) -> bool:
        """Return ``True`` if this node is marked as abstract."""

        return bool(self.payload.get("abstract", False))

    # ------------------------------------------------------------------
    def matches(self, tags: Set[str]) -> bool:
        """Return ``True`` if this node matches ``tags``."""

        node_tags = set(self.payload.get("tags", []))
        node_tags.update({"abstract" if self.is_abstract() else "concrete"})
        return tags.issubset(node_tags)


@define(frozen=True, slots=True)
class Edge:
    """Connection between two nodes."""

    head: str
    tail: str
    directed: bool = False
    payload: dict[str, Any] = field(factory=_payload_factory, hash=False)
