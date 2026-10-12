def generate(rng):
    alphabet = rng.choice(["AB", "ABCDE", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
    text = "".join(rng.choices(alphabet, k=rng.randint(1, 60)))
    return [text, rng.randint(0, len(text))]
