"""Valid seeded inputs for Python/C++ comparison."""


def generate(rng):
    return [[rng.randint(1, 50) for _ in range(rng.randint(1, 12))], rng.randint(1, 30)]
