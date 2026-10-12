def generate(rng):
    rows, cols = rng.randint(1, 4), rng.randint(1, 4)
    return [[[rng.randint(1, 30) for _ in range(cols)] for _ in range(rows)]]
