def generate(rng):
    if rng.random() < 0.1:
        return [rng.sample(range(2, 401, 2), rng.randint(2, 20)), 999]
    # Positive distinct values; at target <= 30 there are at most 2**29 ordered compositions.
    return [rng.sample(range(1, 17), rng.randint(1, 6)), rng.randint(1, 30)]
