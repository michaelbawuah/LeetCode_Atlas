def generate(rng):
    rows, columns = rng.randint(1, 9), rng.randint(1, 9)
    mode = rng.randrange(4)
    return [
        [
            ["0" if mode == 0 else "1" if mode == 1 else rng.choice("01") for _ in range(columns)]
            for _ in range(rows)
        ]
    ]
