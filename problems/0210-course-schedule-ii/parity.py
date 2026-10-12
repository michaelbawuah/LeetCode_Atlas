def generate(rng):
    count = rng.randint(1, 10)
    candidates = [
        (course, before) for course in range(count) for before in range(count) if course != before
    ]
    edges = [
        list(edge) for edge in rng.sample(candidates, rng.randint(0, min(20, len(candidates))))
    ]
    rng.shuffle(edges)
    return [count, edges]
