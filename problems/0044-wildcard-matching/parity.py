def generate(rng):
    text = "".join(rng.choices("abc", k=rng.randint(0, 60)))
    pattern = "".join(rng.choices("abc?*", k=rng.randint(0, 60)))
    if rng.random() < 0.25:
        pattern = "".join(rng.choice([letter, "?", "*"]) for letter in text)
    return [text, pattern]
