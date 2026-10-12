def generate(rng):
    n = rng.randint(1, 8)
    if rng.randrange(5) == 0:
        values = [-268435456, 268435455, -1, 0, 1]
        return [[rng.choice(values) for _ in range(n)] for _ in range(4)]
    return [[rng.randint(-8, 8) for _ in range(n)] for _ in range(4)]
