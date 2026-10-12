def generate(rng):
    size = rng.randint(1, 18)
    if rng.random() < 0.25:
        nums = [rng.choice([-1_000_000_000, 0, 1_000_000_000]) for _ in range(size)]
        target = rng.choice([-1_000_000_000, 0, 1_000_000_000])
    else:
        nums = [rng.randint(-12, 12) for _ in range(size)]
        target = rng.randint(-40, 40)
    return [nums, target]
