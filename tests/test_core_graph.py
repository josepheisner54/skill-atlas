from skill_atlas.core import AtlasGraph, Node, Edge


def test_graph_round_trip() -> None:
    g = AtlasGraph()
    g.add_node(Node(id="a", name="A", description=""))
    g.add_node(Node(id="b", name="B", description=""))
    g.add_edge(Edge(head="b", tail="a", directed=True))

    json_str = g.serialize()
    new_g = AtlasGraph.from_json(json_str)
    assert g == new_g
    assert new_g.is_directed
