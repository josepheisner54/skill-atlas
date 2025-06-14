# skill-atlas

A playground for experimenting with **procedural skill-tree generation**. The project aims to create a flexible graph composition engine where nodes can be expanded into subgraphs according to a set of rewrite rules. Everything is still in the planning stages, but this repository documents the intended layout and upcoming milestones.

## Repository layout

```
skill-atlas/
├─ README.md              ← Project pitch, quick-start, and architecture overview
├─ LICENSE                ← Pick your poison (MIT / Apache-2.0 are friendly)
├─ CONTRIBUTING.md        ← Style guide, branch/PR flow, code-of-conduct
├─ CHANGELOG.md           ← Semantic version history
├─ .gitignore
├─ pyproject.toml         ← Python build metadata (use Poetry or Hatch)
│
├─ src/skill_atlas/       ← Import root (`import skill_atlas as sa`)
│  ├─ __init__.py
│  │
│  ├─ core/               ← Graph primitives
│  │   ├─ node.py         – skill/talent node model
│  │   ├─ edge.py         – dependency/connection model
│  │   └─ graph.py        – immutable graph wrapper + helpers (built on NetworkX)
│  │
│  ├─ grammar/            ← Procedural “rewrite rules” layer
│  │   ├─ rule.py         – base Rule class (match → transform)
│  │   ├─ library.py      – std-lib of canned rules (cluster, mirror, mutate…)
│  │   └─ parser.py       – YAML/JSON → Rule objects
│  │
│  ├─ generator/          ← High-level composition engine
│  │   ├─ atlas_generator.py  – recursive subgraph expansion
│  │   ├─ selector.py         – theme/tier weighting & RNG
│  │   └─ constraints.py      – cycle limits, path length, density caps
│  │
│  ├─ layout/             ← 2-D/3-D positioning algorithms
│  │   ├─ radial.py
│  │   ├─ force_directed.py
│  │   └─ ui_hints.py     – snap-to-grid, group labeling
│  │
│  ├─ export/             ← Target-format emitters
│  │   ├─ json.py
│  │   ├─ godot_scene.py
│  │   ├─ unity_yaml.py
│  │   └─ cytoscape.py    – for quick HTML visualization
│  │
│  ├─ cli/                ← `skill-atlas` console entry-point
│  │   └─ main.py
│  │
│  └─ utils/              ← RNG seeds, logging, profiling, misc helpers
│
├─ data/                  ← Out-of-tree content
│  ├─ subgraphs/          – *.yml templates (e.g. fire.yml, stealth.yml)
│  └─ themes.yml          – theme metadata / weight tables
│
├─ examples/              ← End-to-end demo configs & rendered outputs
│  ├─ minimal/            – one-zone atlas
│  ├─ poe_like/           – 500-node showcase
│  └─ tech_tree/          – 4X strategy demo
│
├─ docs/                  ← MkDocs or Sphinx site
│  ├─ index.md
│  ├─ architecture.md
│  ├─ api/
│  └─ tutorials/
│
└─ tests/                 ← pytest suite
   ├─ unit/
   ├─ integration/
   └─ golden/            – fixtures for deterministic graph snapshots
```

## Graph composition model

At its heart the project treats a skill tree as a directed acyclic graph. Nodes can represent talents, perks, or technology items. Each node may optionally reference another graph template. During generation the **generator** module walks the graph, substituting these templates according to a set of procedural rules. This allows small building blocks to be combined into large atlases without hand‑crafting every connection.

Rules live in the `grammar` package and describe how patterns should be replaced or expanded. A simple example might replace a single "spell" node with a small spell school subgraph, rolled with weighted randomness. More sophisticated rules can cluster nodes, mirror whole sections, or mutate attributes.

The end goal is a reusable toolkit that can output to multiple formats (JSON, Godot scenes, Unity YAML, etc.) after applying a layout algorithm. The current codebase only contains the scaffolding, but the plan is laid out in the source tree and `ROADMAP.md`.

## Contributing

Contributions are welcome! Check the issue templates for guidance on filing bugs or proposing features. The [Roadmap](./ROADMAP.md) lists a few of the high‑level tasks that still need volunteers.
