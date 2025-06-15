from skill_atlas.core.node import Edge, Node


def test_node_equality_and_hashing() -> None:
    node1 = Node(id="n1", name="Node", description="desc")
    node2 = Node(id="n1", name="Node", description="desc")

    assert node1 == node2
    assert hash(node1) == hash(node2)
    assert {node1} == {node2}


def test_edge_equality_and_hashing() -> None:
    edge1 = Edge(head="a", tail="b")
    edge2 = Edge(head="a", tail="b")

    assert edge1 == edge2
    assert hash(edge1) == hash(edge2)
    assert {edge1} == {edge2}
