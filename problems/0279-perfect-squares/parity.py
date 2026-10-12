def generate(rng):
    return [10000 if rng.randrange(30) == 0 else rng.randint(1, 300)]
