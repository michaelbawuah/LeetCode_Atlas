"""Bounded valid histories with varied shapes; independent oracles are in properties."""

import json
from pathlib import Path


def fixture(rng):
    return rng.choice(json.loads(Path(__file__).with_name("cases.json").read_text()))["args"]


def encode(root):
    if root is None:
        return []
    result, pending = [], [root]
    for node in pending:
        if node is None:
            result.append(None)
        else:
            result.append(node["value"])
            pending.extend((node["left"], node["right"]))
    while result and result[-1] is None:
        result.pop()
    return result


def random_tree(rng, values, max_depth=None):
    if not values:
        return None
    root = {"value": values[0], "left": None, "right": None}
    slots = [(root, "left", 2), (root, "right", 2)]
    for value in values[1:]:
        parent, side, depth = slots.pop(rng.randrange(len(slots)))
        child = {"value": value, "left": None, "right": None}
        parent[side] = child
        if max_depth is None or depth < max_depth:
            slots.extend(((child, "left", depth + 1), (child, "right", depth + 1)))
    return root


def leaf_sums(root):
    sums, pending = [], [(root, 0)] if root is not None else []
    while pending:
        node, before = pending.pop()
        total = before + node["value"]
        if node["left"] is None and node["right"] is None:
            sums.append(total)
        for side in ("left", "right"):
            if node[side] is not None:
                pending.append((node[side], total))
    return sums


def generate(rng):
    if rng.randrange(8) == 0:
        return fixture(rng)
    values = [rng.randint(0, 9) for _ in range(rng.randint(1, 40))]
    return [encode(random_tree(rng, values, max_depth=7))]
