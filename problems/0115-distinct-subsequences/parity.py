def generate(rng):
    if rng.random() < 0.05:
        return ["a" * 1000, "a" * 500 + "b"]
    # Any count for at most 24 source positions is below 2**24.
    source = "".join(rng.choices("abAB", k=rng.randint(1, 24)))
    target = "".join(rng.choices("abAB", k=rng.randint(1, 15)))
    if rng.random() < 0.3:
        target = "".join(
            source[i] for i in sorted(rng.sample(range(len(source)), rng.randint(1, len(source))))
        )
    return [source, target]
