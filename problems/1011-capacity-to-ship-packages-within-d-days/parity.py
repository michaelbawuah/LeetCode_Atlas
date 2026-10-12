def generate(rng):
    weights = [rng.randint(1, 500) for _ in range(rng.randint(1, 60))]
    return [weights, rng.randint(1, len(weights))]
