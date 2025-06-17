from __future__ import annotations

from attrs import define, field
import json
import hashlib
import networkx as nx
from typing import Any

from .node import Edge, Node


def _graph_factory() -> nx.MultiDiGraph[Any]:
    return nx.MultiDiGraph()


@define(slots=True)
class AtlasGraph:
    """Immutable wrapper around ``networkx.MultiDiGraph``."""

    _g: nx.MultiDiGraph[Any] = field(factory=_graph_factory)
    _edges: list[Edge] = field(factory=lambda: [], init=False)

    # ------------------------------------------------------------------
    def add_node(self, node: Node) -> None:
        """Add ``node`` to the graph."""
        self._g.add_node(node.id, node=node)  # pyright: ignore[reportUnknownMemberType]

    # ------------------------------------------------------------------
    def add_edge(self, edge: Edge) -> None:
        """Add ``edge`` to the graph."""
        self._g.add_edge(edge.tail, edge.head, edge=edge)  # pyright: ignore[reportUnknownMemberType]
        if not edge.directed:
            self._g.add_edge(edge.head, edge.tail, edge=edge)  # pyright: ignore[reportUnknownMemberType]
        self._edges.append(edge)

    # ------------------------------------------------------------------
    def nodes(self) -> list[Node]:
        node_items = list(self._g.nodes(data=True))
        node_items_sorted: list[tuple[str, dict[str, Any]]] = sorted(node_items)
        return [data["node"] for _, data in node_items_sorted]

    # ------------------------------------------------------------------
    def edges(self) -> list[Edge]:
        return list(self._edges)

    # ------------------------------------------------------------------
    @property
    def is_directed(self) -> bool:
        return any(edge.directed for edge in self.edges())

    # ------------------------------------------------------------------
    def serialize(self) -> str:
        def _edge_key(e: Edge) -> tuple[str, str, bool, str]:
            payload_json = json.dumps(e.payload, sort_keys=True)
            payload_hash = hashlib.sha1(payload_json.encode()).hexdigest()
            return (
                e.tail,
                e.head,
                e.directed,
                payload_hash,
            )

        edges_sorted = sorted(self.edges(), key=_edge_key)

        graph_dict = {
            "nodes": [
                {
                    "id": n.id,
                    "name": n.name,
                    "description": n.description,
                    "icon_path": n.icon_path,
                    "payload": n.payload,
                }
                for n in self.nodes()
            ],
            "edges": [
                {
                    "head": e.head,
                    "tail": e.tail,
                    "directed": e.directed,
                    "payload": e.payload,
                }
                for e in edges_sorted
            ],
        }
        return json.dumps(graph_dict, sort_keys=True)

    # ------------------------------------------------------------------
    @classmethod
    def from_json(cls, data: str) -> "AtlasGraph":
        d: dict[str, Any] = json.loads(data)
        g = cls()
        for node_info in sorted(d["nodes"], key=lambda n: n["id"]):
            g.add_node(
                Node(
                    id=node_info["id"],
                    name=node_info["name"],
                    description=node_info["description"],
                    icon_path=node_info.get("icon_path"),
                    payload=node_info.get("payload", {}),
                )
            )
        for edge_info in d["edges"]:
            g.add_edge(
                Edge(
                    head=edge_info["head"],
                    tail=edge_info["tail"],
                    directed=edge_info.get("directed", False),
                    payload=edge_info.get("payload", {}),
                )
            )
        return g

    # ------------------------------------------------------------------
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AtlasGraph):
            return False
        return self.serialize() == other.serialize()
