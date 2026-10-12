def generate(rng):
    n = rng.randint(1, 6)
    return [[[rng.randint(0, 1) for _ in range(n)] for _ in range(n)]]
