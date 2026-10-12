def generate(rng):
    rows, cols = rng.randint(1, 6), rng.randint(1, 6)
    return [[[rng.randint(0, 1) for _ in range(cols)] for _ in range(rows)]]
