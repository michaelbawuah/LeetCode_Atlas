def generate(rng):
    n = rng.randint(1, 40)
    upper = rng.choice([5, 10000])
    arr = sorted(rng.randint(-upper, upper) for _ in range(n))
    return [arr, rng.randint(1, n), rng.randint(-10000, 10000)]
