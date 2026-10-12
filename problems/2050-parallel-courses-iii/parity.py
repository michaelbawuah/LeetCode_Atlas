def generate(rng):
    n = rng.randint(1, 8)
    edges = [[a, b] for a in range(1, n + 1) for b in range(a + 1, n + 1) if rng.random() < 0.3]
    return [n, edges, [rng.randint(1, 20) for _ in range(n)]]
