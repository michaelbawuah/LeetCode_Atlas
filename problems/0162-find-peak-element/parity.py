def generate(rng):
    values = []
    for _ in range(rng.randint(1, 40)):
        value = rng.randint(-1000, 1000)
        while values and value == values[-1]:
            value = rng.randint(-1000, 1000)
        values.append(value)
    return [values]
