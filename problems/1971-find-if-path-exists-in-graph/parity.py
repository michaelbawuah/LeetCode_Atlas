def generate(rng):
    n = rng.randint(1, 12)
    edges = [[a, b] for a in range(n) for b in range(a + 1, n) if rng.random() < 0.25]
    return [n, edges, rng.randrange(n), rng.randrange(n)]
