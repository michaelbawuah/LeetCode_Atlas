def generate(rng):
    names = ["a", "b", "c", "d"]
    potentials = {name: 2.0 ** rng.randint(-2, 2) for name in names}
    pairs = rng.sample([(a, b) for a in names for b in names if a != b], rng.randint(1, 8))
    equations = [list(pair) for pair in pairs]
    values = [potentials[a] / potentials[b] for a, b in pairs]
    queries = [
        [rng.choice(names + ["x"]), rng.choice(names + ["x"])] for _ in range(rng.randint(1, 8))
    ]
    return [equations, values, queries]
