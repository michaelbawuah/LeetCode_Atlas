def generate(rng):
    values = [rng.randint(0, 100000) for _ in range(rng.randint(1, 80))]
    if rng.random() < 0.2:
        values.sort(reverse=rng.choice([True, False]))
    return [values]
