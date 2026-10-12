"""Generate valid inputs for reproducible cross-language comparisons."""


def generate(rng):
    length = rng.randint(1, 80)
    first = "".join(rng.choices("abc123!?", k=length))
    if rng.random() < 0.5:
        alphabet = "abc123!?"
        values = rng.sample(list("xyz456@#"), len(alphabet))
        mapping = dict(zip(alphabet, values, strict=True))
        second = "".join(mapping[c] for c in first)
    else:
        second = "".join(rng.choices("xyz456@#", k=length))
    return [first, second]
