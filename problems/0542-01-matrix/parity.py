def generate(rng):
    rows, cols = rng.randint(1, 6), rng.randint(1, 6)
    mat = [[rng.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
    mat[rng.randrange(rows)][rng.randrange(cols)] = 0
    return [mat]
