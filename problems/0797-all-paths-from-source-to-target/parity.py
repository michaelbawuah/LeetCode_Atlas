def generate(rng):
    count = rng.randint(2, 6)
    graph = [[] for _ in range(count)]
    for first in range(count):
        for last in range(first + 1, count):
            if rng.random() < 0.45:
                graph[first].append(last)
    return [graph]
