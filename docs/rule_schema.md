# Rule DSL

Rules are described in YAML. Each rule defines:

- `match`: list of tags that a node must contain to trigger the rule.
- `replace`: subgraph inserted when the rule fires. It contains `nodes` and `edges` using the same fields as `AtlasGraph` JSON.
- `probability`: optional float between 0 and 1 controlling how often the rule applies. Defaults to `1`.

```yaml
- match: [abstract, foo]
  replace:
    nodes:
      - id: child
        name: Child Node
        description: Example node
    edges: []
  probability: 0.5
```
