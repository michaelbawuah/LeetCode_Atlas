def generate(rng):
    values = [rng.randint(0, 50) for _ in range(rng.randint(1, 20))]
    if rng.random() < 0.2:
        values = [0] * len(values)
    target = rng.randint(-1000, 1000)
    if rng.random() < 0.5:
        target = sum(value * rng.choice([-1, 1]) for value in values)
    return [values, target]
