"""Valid seeded inputs for Python/C++ comparison."""


def generate(rng):
    size = rng.randint(1, 100)
    text = "".join(rng.choice("abcXYZ,.") for _ in range(size))
    return [text, rng.choice([1, size, size + 1, rng.randint(1, 1000)])]
