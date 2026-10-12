"""Generate valid inputs for reproducible cross-language comparisons."""


def generate(rng):
    return [
        rng.choice([-(2**31), 2**31 - 1, 1534236469, -2147483412, 0, 120])
        if rng.random() < 0.3
        else rng.randint(-(2**31), 2**31 - 1)
    ]
