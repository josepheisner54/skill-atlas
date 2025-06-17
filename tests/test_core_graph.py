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


def test_edge_sorting_deterministic() -> None:
    g1 = AtlasGraph()
    g2 = AtlasGraph()

    for g in (g1, g2):
        g.add_node(Node(id="a", name="A", description=""))
        g.add_node(Node(id="b", name="B", description=""))
        g.add_node(Node(id="c", name="C", description=""))

    edge1 = Edge(head="b", tail="a", payload={"p": 1})
    edge2 = Edge(head="c", tail="b", payload={"p": 2})

    g1.add_edge(edge1)
    g1.add_edge(edge2)

    g2.add_edge(edge2)
    g2.add_edge(edge1)

    assert g1.serialize() == g2.serialize()
