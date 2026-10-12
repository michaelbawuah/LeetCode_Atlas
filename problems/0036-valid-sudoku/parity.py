def generate(rng):
    if rng.random() < 0.5:
        digits = rng.sample("123456789", 9)
        board = [
            [digits[(row * 3 + row // 3 + column) % 9] for column in range(9)] for row in range(9)
        ]
        holes = rng.sample(range(81), rng.randint(0, 81))
        for index in holes:
            board[index // 9][index % 9] = "."
    else:
        board = [["."] * 9 for _ in range(9)]
        for index in rng.sample(range(81), rng.randint(0, 81)):
            board[index // 9][index % 9] = rng.choice("123456789")
    return [board]
