def generate(rng):
    n = rng.randint(2, 10)
    pairs = [[a, b] for a in range(n) for b in range(a + 1, n)]
    return [n, rng.sample(pairs, rng.randint(1, len(pairs)))]
