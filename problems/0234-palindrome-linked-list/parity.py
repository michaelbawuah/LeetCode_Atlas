"""Bounded valid histories with varied shapes; independent oracles are in properties."""

import json
from pathlib import Path


def fixture(rng):
    return rng.choice(json.loads(Path(__file__).with_name("cases.json").read_text()))["args"]


def generate(rng):
    if rng.randrange(8) == 0:
        return fixture(rng)
    half = [rng.randint(0, 9) for _ in range(rng.randint(0, 60))]
    if rng.random() < 0.55:
        middle = [rng.randint(0, 9)] if rng.random() < 0.5 else []
        values = half + middle + half[::-1]
        return [values or [rng.randint(0, 9)]]
    return [[rng.randint(0, 9) for _ in range(rng.randint(1, 120))]]
