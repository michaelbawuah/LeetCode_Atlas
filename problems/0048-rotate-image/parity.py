def generate(rng):
    size = rng.randint(1, 10)
    return [[[rng.randint(-1000, 1000) for _ in range(size)] for _ in range(size)]]
