"""Generate valid inputs for reproducible cross-language comparisons."""


def generate(rng):
    return [bin(rng.getrandbits(rng.randint(1, 150)))[2:] for _ in range(2)]
