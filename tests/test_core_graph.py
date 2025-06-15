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


def test_graph_round_trip_with_abstract_node() -> None:
    g = AtlasGraph()
    g.add_node(Node(id="a", name="A", description="", payload={"abstract": True}))
    g.add_node(Node(id="b", name="B", description=""))
    g.add_edge(Edge(head="b", tail="a"))

    json_str = g.serialize()
    new_g = AtlasGraph.from_json(json_str)
    assert g == new_g
    abstract_nodes = [n for n in new_g.nodes() if n.is_abstract()]
    assert len(abstract_nodes) == 1
