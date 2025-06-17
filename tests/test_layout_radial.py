from skill_atlas.layout.radial import radial_layout
import networkx as nx
from typing import Any


def test_radial_layout_positions() -> None:
    g: nx.Graph[Any] = nx.Graph()
    for i in range(4):
        g.add_node(i)

    positions = radial_layout(g)
    assert len(positions) == 4
    for pos in positions.values():
        assert isinstance(pos[0], float) and isinstance(pos[1], float)
