"""Command-line interface for skill-atlas."""

from __future__ import annotations

import argparse
import importlib.metadata
from typing import Any

import networkx as nx


def build_graph(n: int) -> nx.Graph[Any]:
    """Return a simple graph with ``n`` nodes."""
    g: nx.Graph[Any] = nx.Graph()
    g.add_nodes_from(range(n))  # pyright: ignore[reportUnknownMemberType]
    return g


def run(argv: list[str] | None = None) -> None:
    """Run the skill-atlas CLI."""
    parser = argparse.ArgumentParser(description="Skill atlas generator")
    parser.add_argument(
        "--nodes",
        type=int,
        default=0,
        help="Number of nodes in a sample graph to generate",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"skill-atlas {importlib.metadata.version('skill-atlas')}",
    )
    args = parser.parse_args(argv)
    g = build_graph(args.nodes)
    print(f"generated graph with {g.number_of_nodes()} nodes")


if __name__ == "__main__":
    run()
