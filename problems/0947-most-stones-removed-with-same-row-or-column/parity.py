def generate(rng):
    coordinates = [(r, c) for r in range(5) for c in range(5)]
    return [[list(point) for point in rng.sample(coordinates, rng.randint(1, 12))]]
