"""Bounded valid histories with varied shapes; independent oracles are in properties."""

import json
from pathlib import Path


def fixture(rng):
    return rng.choice(json.loads(Path(__file__).with_name("cases.json").read_text()))["args"]


def generate(rng):
    if rng.randrange(8) == 0:
        return fixture(rng)
    values = [rng.randint(-500, 500) for _ in range(rng.randint(1, 120))]
    left = rng.randint(1, len(values))
    return [values, left, rng.randint(left, len(values))]
