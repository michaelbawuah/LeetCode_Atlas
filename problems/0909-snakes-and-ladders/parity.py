def generate(rng):
    size = rng.randint(2, 3)
    board = [[-1] * size for _ in range(size)]
    for label in range(2, size * size):
        if rng.random() < 0.3:
            below, col = divmod(label - 1, size)
            if below % 2:
                col = size - 1 - col
            board[size - 1 - below][col] = rng.randint(1, size * size)
    return [board]
