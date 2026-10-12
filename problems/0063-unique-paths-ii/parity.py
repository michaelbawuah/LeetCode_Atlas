def generate(rng):
    if rng.randrange(12) == 0:
        grid = [[0] * 40 for _ in range(40)]
        grid[-1][-1] = 1
        return [grid]
    rows, columns = rng.randint(1, 8), rng.randint(1, 8)
    mode = rng.randrange(4)
    return [
        [
            [
                0 if mode == 0 else 1 if mode == 1 else int(rng.random() < 0.3)
                for _ in range(columns)
            ]
            for _ in range(rows)
        ]
    ]
