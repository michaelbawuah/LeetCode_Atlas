def generate(rng):
    rows, columns = rng.randint(1, 10), rng.randint(1, 10)
    values = [-2_147_483_648, -1, 0, 0, 1, 2_147_483_647]
    return [[[rng.choice(values) for _ in range(columns)] for _ in range(rows)]]
