def generate(rng):
    mode = rng.randrange(4)
    if mode == 0:
        text = rng.choice("abA019") * rng.randint(1, 80)
    elif mode == 1:
        half = "".join(rng.choices("abcA019", k=rng.randint(1, 20)))
        text = half + rng.choice(["", "x"]) + half[::-1]
    else:
        text = "".join(rng.choices("abcABC019", k=rng.randint(1, 80)))
    return [text]
