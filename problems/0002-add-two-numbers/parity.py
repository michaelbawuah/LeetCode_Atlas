"""Generate bounded valid inputs; answer oracles live in the property suite."""

import json
from pathlib import Path


def generate(rng):
    if rng.randrange(8) == 0:
        cases = json.loads(Path(__file__).with_name("cases.json").read_text())
        return rng.choice(cases)["args"]

    def digits():
        length = rng.randint(1, 40)
        values = [rng.randint(0, 9) for _ in range(length)]
        if length > 1:
            values[-1] = rng.randint(1, 9)
        return values

    return [digits(), digits()]
