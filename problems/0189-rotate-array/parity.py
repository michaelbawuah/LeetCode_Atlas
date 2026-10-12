def generate(rng):
    values = [rng.randint(-2_147_483_648, 2_147_483_647) for _ in range(rng.randint(1, 40))]
    k = rng.choice([0, len(values), len(values) + 1, rng.randint(0, 100_000)])
    return [values, k]
