def generate(rng):
    trips = []
    for _ in range(rng.randint(1, 20)):
        start = rng.randint(0, 999)
        end = rng.randint(start + 1, 1000)
        trips.append([rng.randint(1, 100), start, end])
    return [trips, rng.choice([rng.randint(1, 100), rng.randint(1, 100000)])]
