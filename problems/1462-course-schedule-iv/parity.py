def generate(rng):
    n = rng.randint(2, 8)
    edges = [[a, b] for a in range(n) for b in range(a + 1, n) if rng.random() < 0.35]
    queries = rng.sample(
        [[a, b] for a in range(n) for b in range(n) if a != b], rng.randint(1, min(15, n * (n - 1)))
    )
    return [n, edges, queries]
