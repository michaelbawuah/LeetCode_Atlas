"""Generate valid inputs for reproducible cross-language comparisons."""


def generate(rng):
    if rng.random() < 0.4:
        half = str(rng.randint(1, 9999))
        return [int(half + half[::-1])]
    return [rng.randint(-(2**31), 2**31 - 1)]
