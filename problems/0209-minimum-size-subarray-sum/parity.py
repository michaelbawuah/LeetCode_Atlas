def generate(rng):
    values = [rng.randint(1, 10_000) for _ in range(rng.randint(1, 60))]
    target = rng.choice([1, sum(values), sum(values) + 1, rng.randint(1, 1_000_000_000)])
    return [target, values]
