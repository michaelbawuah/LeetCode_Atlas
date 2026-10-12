"""Generate bounded valid inputs; answer oracles live in the property suite."""

import json
from pathlib import Path


def encode(root):
    if root is None:
        return []
    pending, result = [root], []
    for node in pending:
        if node is None:
            result.append(None)
        else:
            result.append(node["value"])
            pending.extend((node["left"], node["right"]))
    while result and result[-1] is None:
        result.pop()
    return result


def random_tree(rng, count, low, high):
    if count == 0:
        return []
    root = {"value": rng.randint(low, high), "left": None, "right": None}
    slots = [(root, "left"), (root, "right")]
    for _ in range(count - 1):
        parent, field = slots.pop(rng.randrange(len(slots)))
        child = {"value": rng.randint(low, high), "left": None, "right": None}
        parent[field] = child
        slots.extend(((child, "left"), (child, "right")))
    return encode(root)


def random_bst(values):
    root = None
    for value in values:
        if root is None:
            root = {"value": value, "left": None, "right": None}
            continue
        node = root
        while True:
            field = "left" if value < node["value"] else "right"
            if node[field] is None:
                node[field] = {"value": value, "left": None, "right": None}
                break
            node = node[field]
    return encode(root)


def generate(rng):
    if rng.randrange(8) == 0:
        cases = json.loads(Path(__file__).with_name("cases.json").read_text())
        return rng.choice(cases)["args"]
    return [random_tree(rng, rng.randint(1, 45), -100, 100)]
