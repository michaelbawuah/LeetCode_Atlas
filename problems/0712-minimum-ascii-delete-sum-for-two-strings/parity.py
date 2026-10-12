def generate(rng):
    first = "".join(rng.choice("azbc") for _ in range(rng.randint(1, 20)))
    second = (
        first
        if rng.randrange(4) == 0
        else "".join(rng.choice("azbc") for _ in range(rng.randint(1, 20)))
    )
    return [first, second]
