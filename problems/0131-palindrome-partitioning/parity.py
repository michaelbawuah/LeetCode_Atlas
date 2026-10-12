"""Valid seeded inputs for Python/C++ comparison."""


def generate(rng):
    return ["".join(rng.choice("abc") for _ in range(rng.randint(1, 12)))]
