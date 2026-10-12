def generate(rng):
    if rng.random() < 0.1:
        # Enormous counts in valid prefixes, followed by an invalid final "00".
        return ["1" * 98 + "00"]
    return ["".join(rng.choices("0123456789", k=rng.randint(1, 30)))]
