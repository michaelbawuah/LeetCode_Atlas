def generate(rng):
    count = rng.randint(1, 8)
    graph = [[last for last in range(count) if rng.random() < 0.25] for _ in range(count)]
    if not any(graph):
        graph[0] = [0]
    return [graph]
