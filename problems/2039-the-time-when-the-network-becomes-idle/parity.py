def generate(rng):
    n = rng.randint(2, 9)
    edges = [[node, rng.randrange(node)] for node in range(1, n)]
    extra = [
        [a, b]
        for a in range(n)
        for b in range(a + 1, n)
        if [b, a] not in edges and [a, b] not in edges
    ]
    edges += rng.sample(extra, rng.randint(0, min(5, len(extra))))
    return [edges, [0] + [rng.randint(1, 8) for _ in range(n - 1)]]
