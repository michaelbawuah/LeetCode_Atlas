def generate(rng):
    rows, columns = rng.randint(1, 10), rng.randint(1, 10)
    return [[[rng.randint(-100, 100) for _ in range(columns)] for _ in range(rows)]]
