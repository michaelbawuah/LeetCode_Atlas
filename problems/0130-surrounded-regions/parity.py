def generate(rng):
    rows, cols = rng.randint(1, 8), rng.randint(1, 8)
    density = rng.choice((0.0, 0.25, 0.5, 0.75, 1.0))
    board = [["O" if rng.random() < density else "X" for _ in range(cols)] for _ in range(rows)]
    return [board]
