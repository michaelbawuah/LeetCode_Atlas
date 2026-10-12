def generate(rng):
    rows, columns = rng.randint(1, 8), rng.randint(1, 8)
    matrix = [[0] * columns for _ in range(rows)]
    initial = rng.randint(-30, 0)
    for row in range(rows):
        for column in range(columns):
            above = matrix[row - 1][column] if row else initial
            before = matrix[row][column - 1] if column else initial
            matrix[row][column] = max(above, before) + rng.randint(0, 8)
    target = (
        rng.choice(rng.choice(matrix))
        if rng.randrange(2)
        else rng.randint(initial - 1, matrix[-1][-1] + 1)
    )
    return [matrix, target]
