def generate(rng):
    n = rng.randint(1, 8)
    edges = [[a, b] for a in range(n) for b in range(a + 1, n) if rng.random() < 0.4]
    return [n, edges]
