def generate(rng):
    n = rng.randint(2, 9)
    edges = [[node, rng.randrange(node)] for node in range(1, n)]
    extras = [
        [a, b]
        for a in range(n)
        for b in range(a + 1, n)
        if [a, b] not in edges and [b, a] not in edges
    ]
    edges += rng.sample(extras, rng.randint(0, min(5, len(extras))))
    rng.shuffle(edges)
    return [n, edges]
