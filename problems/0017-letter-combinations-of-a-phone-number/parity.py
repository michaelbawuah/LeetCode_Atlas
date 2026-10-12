"""Valid seeded inputs for Python/C++ comparison."""


def generate(rng):
    return ["".join(rng.choice("23456789") for _ in range(rng.randint(1, 4)))]
