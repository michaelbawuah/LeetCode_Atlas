def generate(rng):
    size = rng.randint(2, 6)
    first = (rng.randrange(size), rng.randrange(size))
    choices = [
        (r, c)
        for r in range(size)
        for c in range(size)
        if abs(r - first[0]) + abs(c - first[1]) > 1
    ]
    if not choices:
        first = (0, 0)
        choices = [(size - 1, size - 1)]
    last = rng.choice(choices)
    grid = [[0] * size for _ in range(size)]
    grid[first[0]][first[1]] = grid[last[0]][last[1]] = 1
    return [grid]
