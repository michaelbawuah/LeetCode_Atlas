def generate(rng):
    universe = [a + b for a in "abc" for b in "abc"]
    begin, end = rng.sample(universe, 2)
    return [begin, end, rng.sample(universe, rng.randint(1, 7))]
