def generate(rng):
    if rng.random() < 0.15:
        return [rng.choice([-1.0, 1.0]), rng.choice([-2147483648, 2147483647])]
    base = rng.choice([-3.0, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 3.0])
    exponent = rng.randint(1, 6) if base == 0 else rng.randint(-6, 6)
    # These pairs stay in the official result interval [-10000, 10000].
    return [base, exponent]
