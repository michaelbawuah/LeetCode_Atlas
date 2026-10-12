def generate(rng):
    count = rng.randint(1, 12)
    edges = [[node, rng.randrange(node)] for node in range(1, count)]
    rng.shuffle(edges)
    return [count, edges]
