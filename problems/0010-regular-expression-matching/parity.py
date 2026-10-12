def generate(rng):
    text = "".join(rng.choices("abc", k=rng.randint(1, 20)))
    atoms = []
    for _ in range(rng.randint(1, 10)):
        atoms.append(rng.choice("abc.") + ("*" if rng.random() < 0.5 else ""))
    return [text, "".join(atoms)]
