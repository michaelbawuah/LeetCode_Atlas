def generate(rng):
    rows, columns = rng.randint(1, 10), rng.randint(1, 10)
    zero = rng.randrange(5) == 0
    return [[[0 if zero else rng.randint(0, 200) for _ in range(columns)] for _ in range(rows)]]
