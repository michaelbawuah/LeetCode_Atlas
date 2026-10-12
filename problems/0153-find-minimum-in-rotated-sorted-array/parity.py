def generate(rng):
    values = sorted(rng.sample(range(-5000, 5001), rng.randint(1, 40)))
    pivot = rng.randrange(len(values))
    return [values[pivot:] + values[:pivot]]
