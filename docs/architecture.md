# Architecture

This document describes the core design decisions of the project.

## Undirected edges

Undirected connections are stored only once in ``AtlasGraph._edges`` but are inserted twice into the underlying ``networkx.MultiDiGraph`` (``tail``→``head`` and ``head``→``tail``). This mirror approach keeps edge iteration stable while still letting ``NetworkX`` return neighbors in both directions. Future validators should treat the two directed edges as a single logical connection and not flag them as duplicates.
