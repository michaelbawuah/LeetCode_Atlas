def generate(rng):
    upper = rng.choice([5, 1000])
    return [
        [rng.randint(0, upper) for _ in range(rng.randint(1, 30))],
        [rng.randint(0, upper) for _ in range(rng.randint(1, 30))],
    ]
