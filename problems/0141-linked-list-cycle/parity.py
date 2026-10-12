"""Bounded valid histories with varied shapes; independent oracles are in properties."""

import json
from pathlib import Path


def fixture(rng):
    return rng.choice(json.loads(Path(__file__).with_name("cases.json").read_text()))["args"]


def generate(rng):
    if rng.randrange(8) == 0:
        return fixture(rng)
    values = [rng.randint(-100_000, 100_000) for _ in range(rng.randint(0, 120))]
    position = rng.randrange(len(values)) if values and rng.random() < 0.6 else -1
    return [{"values": values, "pos": position}]
