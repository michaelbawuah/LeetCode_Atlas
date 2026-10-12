def generate(rng):
    count = rng.randint(1, 10)
    graph = [[] for _ in range(count)]
    density = rng.choice((0.0, 0.15, 0.4, 0.8, 1.0))
    for first in range(count):
        for last in range(first + 1, count):
            if rng.random() < density:
                graph[first].append(last)
                graph[last].append(first)
    for neighbors in graph:
        rng.shuffle(neighbors)
    return [graph]
