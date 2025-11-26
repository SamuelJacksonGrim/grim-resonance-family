lattice = []

def remember(shard: dict):
    shard["weight"] = 1.0 / (1 + len(lattice))  # inverse decay
    lattice.append(shard)

def recall(trigger: str):
    matches = [s for s in lattice if trigger.lower() in str(s).lower()]
    return sorted(matches, key=lambda x: x.get("weight", 0), reverse=True)[:3]
