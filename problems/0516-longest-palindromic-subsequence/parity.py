def generate(rng):
    size = rng.randint(1, 35)
    return [
        "a" * size if rng.randrange(4) == 0 else "".join(rng.choice("abc") for _ in range(size))
    ]
