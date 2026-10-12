"""Generate valid inputs for reproducible cross-language comparisons."""


def generate(rng):
    return [[rng.choice("abcXYZ012!? ") for _ in range(rng.randint(1, 100))]]
