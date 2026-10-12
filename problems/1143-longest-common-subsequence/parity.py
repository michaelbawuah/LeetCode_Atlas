def generate(rng):
    first = "".join(rng.choices("abcd", k=rng.randint(1, 60)))
    second = "".join(rng.choices("abcd", k=rng.randint(1, 60)))
    if rng.random() < 0.3:
        second = "".join(
            first[i] for i in sorted(rng.sample(range(len(first)), rng.randint(1, len(first))))
        )
    return [first, second]
