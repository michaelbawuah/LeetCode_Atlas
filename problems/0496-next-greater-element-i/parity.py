"""Generate valid inputs for reproducible cross-language comparisons."""


def generate(rng):
    values = rng.sample(range(10001), rng.randint(1, 40))
    return [rng.sample(values, rng.randint(1, len(values))), values]
