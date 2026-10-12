def generate(rng):
    height = rng.randint(1, 10)
    return [[[rng.randint(-10000, 10000) for _ in range(row)] for row in range(1, height + 1)]]
