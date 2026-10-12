def generate(rng):
    rows, cols = rng.randint(1, 4), rng.randint(1, 4)
    maze = [[rng.choice(".+") for _ in range(cols)] for _ in range(rows)]
    entrance = [rng.randrange(rows), rng.randrange(cols)]
    maze[entrance[0]][entrance[1]] = "."
    return [maze, entrance]
