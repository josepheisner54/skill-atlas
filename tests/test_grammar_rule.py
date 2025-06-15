from pathlib import Path

from skill_atlas.core import Node
from skill_atlas.grammar import load_rules


RULES_PATH = Path(__file__).resolve().parent.parent / "examples" / "rules.yaml"


def test_load_rules() -> None:
    rules = load_rules(RULES_PATH)
    assert len(rules) == 2


def test_rule_applies() -> None:
    rules = load_rules(RULES_PATH)
    rule = rules[0]
    abstract_node = Node(id="a", name="A", description="", payload={"abstract": True})
    concrete_node = Node(id="b", name="B", description="")

    assert rule.applies(abstract_node)
    assert not rule.applies(concrete_node)
