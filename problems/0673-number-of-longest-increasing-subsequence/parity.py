def generate(rng):
    if rng.random() < 0.1:
        # 2**70 longest positive-prefix selections, then one longer negative chain.
        return [[value for value in range(1, 71) for _ in range(2)] + list(range(-71, 0))]
    # Position selections are bounded by 2**30 for these ordinary cases.
    values = [rng.randint(-1000000, 1000000) for _ in range(rng.randint(1, 30))]
    if rng.random() < 0.25:
        values = [rng.randint(-5, 5) for _ in values]
    return [values]
