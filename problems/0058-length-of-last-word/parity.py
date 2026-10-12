"""Generate valid inputs for reproducible cross-language comparisons."""


def generate(rng):
    words = [
        "".join(rng.choices("abcXYZ", k=rng.randint(1, 20))) for _ in range(rng.randint(1, 10))
    ]
    return [
        " " * rng.randint(0, 6) + (" " * rng.randint(1, 5)).join(words) + " " * rng.randint(0, 6)
    ]
