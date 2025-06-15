from __future__ import annotations

from attrs import define
from pathlib import Path
from typing import Set
import yaml

from ..core import AtlasGraph, Node, Edge


def _graph_from_dict(data: dict) -> AtlasGraph:
    g = AtlasGraph()
    for node_info in data.get("nodes", []):
        g.add_node(
            Node(
                id=node_info["id"],
                name=node_info["name"],
                description=node_info.get("description", ""),
                icon_path=node_info.get("icon_path"),
                payload=node_info.get("payload", {}),
            )
        )
    for edge_info in data.get("edges", []):
        g.add_edge(
            Edge(
                head=edge_info["head"],
                tail=edge_info["tail"],
                directed=edge_info.get("directed", False),
                payload=edge_info.get("payload", {}),
            )
        )
    return g


@define(slots=True)
class Rule:
    """Rewrite rule for expanding nodes."""

    match: Set[str]
    replace: AtlasGraph
    probability: float = 1.0

    # --------------------------------------------------------------
    def applies(self, node: Node) -> bool:
        """Return ``True`` if this rule can be applied to ``node``."""

        return node.matches(self.match)

    # --------------------------------------------------------------
    def apply(self, graph: AtlasGraph, node_id: str, rng) -> AtlasGraph:
        """Return replacement subgraph for ``node_id`` using ``rng`` for sampling."""

        node = graph._g.nodes[node_id]["node"]  # pyright: ignore[reportPrivateUsage]
        if not self.applies(node):
            raise ValueError("rule does not apply to node")
        if rng.random() > self.probability:
            return AtlasGraph()
        return AtlasGraph.from_json(self.replace.serialize())


# --------------------------------------------------------------
def load_rules(path: Path | str) -> list[Rule]:
    """Load rules from a YAML file."""

    p = Path(path)
    data = yaml.safe_load(p.read_text()) or []
    rules: list[Rule] = []
    for r in data:
        match = set(r.get("match", []))
        replace = _graph_from_dict(r.get("replace", {}))
        prob = float(r.get("probability", 1))
        rules.append(Rule(match=match, replace=replace, probability=prob))
    return rules
