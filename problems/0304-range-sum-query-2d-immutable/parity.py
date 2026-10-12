"""Valid seeded inputs for Python/C++ comparison."""


def generate(rng):
    rows, columns = rng.randint(1, 12), rng.randint(1, 12)
    matrix = [[rng.randint(-10000, 10000) for _ in range(columns)] for _ in range(rows)]
    operations, arguments = ["NumMatrix"], [[matrix]]
    for _ in range(rng.randint(1, 60)):
        row1, row2 = sorted([rng.randrange(rows), rng.randrange(rows)])
        col1, col2 = sorted([rng.randrange(columns), rng.randrange(columns)])
        operations.append("sumRegion")
        arguments.append([row1, col1, row2, col2])
    return [operations, arguments]
