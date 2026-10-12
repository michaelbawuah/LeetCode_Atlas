def generate(rng):
    rows, cols = rng.randint(1, 8), rng.randint(1, 8)
    density = rng.choice((0.0, 0.25, 0.5, 0.75, 1.0))
    grid = [["1" if rng.random() < density else "0" for _ in range(cols)] for _ in range(rows)]
    return [grid]
