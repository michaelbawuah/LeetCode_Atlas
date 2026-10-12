def generate(rng):
    text = "".join(rng.choices("abcd", k=rng.randint(1, 60)))
    if rng.random() < 0.2:
        half = "".join(rng.choices("abcd", k=rng.randint(1, 30)))
        text = half + rng.choice(["", "a"]) + half[::-1]
    return [text]
