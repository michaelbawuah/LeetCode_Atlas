def generate(rng):
    first = "".join(rng.choices("abcdefghijklmnopqrstuvwxyz", k=rng.randint(1, 15)))
    if rng.random() < 0.5:
        middle = "".join(rng.sample(first, len(first)))
        prefix = "".join(rng.choices("abcdefghijklmnopqrstuvwxyz", k=rng.randint(0, 15)))
        suffix = "".join(rng.choices("abcdefghijklmnopqrstuvwxyz", k=rng.randint(0, 15)))
        second = prefix + middle + suffix
    else:
        second = "".join(rng.choices("abcdefghijklmnopqrstuvwxyz", k=rng.randint(1, 45)))
    return [first, second]
