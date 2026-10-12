def generate(rng):
    first = sorted(rng.randint(-1_000_000, 1_000_000) for _ in range(rng.randint(0, 30)))
    second = sorted(rng.randint(-1_000_000, 1_000_000) for _ in range(rng.randint(0, 30)))
    if not first and not second:
        second = [rng.randint(-1_000_000, 1_000_000)]
    if rng.random() < 0.3:
        first = sorted(rng.choice([-1_000_000, 0, 1_000_000]) for _ in first)
        second = sorted(rng.choice([-1_000_000, 0, 1_000_000]) for _ in second)
    return [first, second]
