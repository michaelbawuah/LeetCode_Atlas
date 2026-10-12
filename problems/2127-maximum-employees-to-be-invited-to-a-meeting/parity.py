def generate(rng):
    n = rng.randint(2, 7)
    return [[rng.choice([other for other in range(n) if other != node]) for node in range(n)]]
