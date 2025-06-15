"""Example script demonstrating a small set of Path of Exile skill nodes."""

import json
from pathlib import Path

# Load nodes from the adjacent JSON file
with Path(__file__).with_name("path_of_exile_nodes.json").open() as f:
    POE_NODES = json.load(f)

if __name__ == "__main__":
    for node_id, data in POE_NODES.items():
        print(f"{node_id}: {data['name']}")
        for stat in data.get("stats", []):
            print(f"  - {stat}")
