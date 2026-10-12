def generate(rng):
    count = rng.randint(2, 9)
    candidates = [(first, last) for first in range(count) for last in range(count) if first != last]
    pairs = rng.sample(candidates, rng.randint(0, min(24, count * (count - 1) // 2)))
    flights = [[first, last, rng.randint(1, 10_000)] for first, last in pairs]
    source, target = rng.sample(range(count), 2)
    return [count, flights, source, target, rng.randint(0, count - 1)]
