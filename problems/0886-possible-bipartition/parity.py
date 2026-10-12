def generate(rng):
    count = rng.randint(1, 8)
    edges = [
        [a, b] for a in range(1, count + 1) for b in range(a + 1, count + 1) if rng.random() < 0.35
    ]
    return [count, edges]
