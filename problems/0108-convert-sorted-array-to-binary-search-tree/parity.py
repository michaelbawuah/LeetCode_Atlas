"""Bounded valid histories with varied shapes; independent oracles are in properties."""

import json
from pathlib import Path


def fixture(rng):
    return rng.choice(json.loads(Path(__file__).with_name("cases.json").read_text()))["args"]


def generate(rng):
    if rng.randrange(8) == 0:
        return fixture(rng)
    return [sorted(rng.sample(range(-10_000, 10_001), rng.randint(1, 120)))]
