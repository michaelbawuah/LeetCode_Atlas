"""Valid seeded inputs for Python/C++ comparison."""


def generate(rng):
    return [[rng.randint(-10, 10) for _ in range(rng.randint(1, 10))]]
