def generate(rng):
    rows, cols = rng.randint(1, 7), rng.randint(1, 7)
    return [[[rng.randint(0, 20) for _ in range(cols)] for _ in range(rows)]]
