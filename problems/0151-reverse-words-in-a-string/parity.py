"""Generate valid inputs for reproducible cross-language comparisons."""


def generate(rng):
    words = [
        "".join(rng.choices("abcXYZ012", k=rng.randint(1, 10))) for _ in range(rng.randint(1, 12))
    ]
    return ["  " + (" " * rng.randint(1, 5)).join(words) + " "]
