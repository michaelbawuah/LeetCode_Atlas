def generate(rng):
    size = rng.randint(1, 4)
    return [["".join(rng.choice((" ", "/", chr(92))) for _ in range(size)) for _ in range(size)]]
