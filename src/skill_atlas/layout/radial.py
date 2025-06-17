from __future__ import annotations

from math import cos, sin, tau
from typing import Any

import networkx as nx


def radial_layout(
    graph: nx.Graph[Any], radius: float = 1.0
) -> dict[Any, tuple[float, float]]:
    """Return positions for nodes arranged evenly on a circle."""

    n = graph.number_of_nodes()
    if n == 0:
        return {}

    angle_step = tau / n
    positions: dict[Any, tuple[float, float]] = {}
    for idx, node in enumerate(sorted(graph.nodes())):
        angle = idx * angle_step
        positions[node] = (radius * cos(angle), radius * sin(angle))
    return positions
