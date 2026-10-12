def generate(rng):
    upper = 12 if rng.randrange(2) else 10000
    return [[rng.randint(1, upper) for _ in range(rng.randint(1, 100))]]
