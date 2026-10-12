"""Generate bounded valid inputs; answer oracles live in the property suite."""

import json
from pathlib import Path


def generate(rng):
    if rng.randrange(8) == 0:
        cases = json.loads(Path(__file__).with_name("cases.json").read_text())
        return rng.choice(cases)["args"]
    return [
        [
            sorted(rng.randint(-10000, 10000) for _ in range(rng.randint(0, 25)))
            for _ in range(rng.randint(0, 12))
        ]
    ]
