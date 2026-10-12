"""Valid seeded inputs for Python/C++ comparison."""


def generate(rng):
    return [[rng.randint(-3, 3) for _ in range(rng.randint(1, 8))]]
