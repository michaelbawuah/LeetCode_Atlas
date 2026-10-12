def generate(rng):
    limit = rng.randint(1, 30_000)
    people = [rng.randint(1, limit) for _ in range(rng.randint(1, 40))]
    if rng.random() < 0.25:
        people = [rng.choice([1, limit]) for _ in people]
    return [people, limit]
