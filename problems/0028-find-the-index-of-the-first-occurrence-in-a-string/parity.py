"""Generate valid inputs for reproducible cross-language comparisons."""


def generate(rng):
    if rng.random() < 0.15:
        return ["abababacaba", "ababaca"]
    text = "".join(rng.choices("abc", k=rng.randint(1, 100)))
    if rng.random() < 0.5:
        start = rng.randrange(len(text))
        needle = text[start : rng.randint(start + 1, len(text))]
    else:
        needle = "".join(rng.choices("abc", k=rng.randint(1, 25)))
    return [text, needle]
