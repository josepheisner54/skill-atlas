# skill-atlas
Procedural skill-atlas generator


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
