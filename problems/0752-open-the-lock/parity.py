def generate(rng):
    target = "00" + str(rng.randrange(3)) + str(rng.randrange(3))
    candidates = [f"{value:04d}" for value in range(30)] + ["9999"]
    return [
        rng.sample([state for state in candidates if state != target], rng.randint(1, 7)),
        target,
    ]
