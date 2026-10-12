def generate(rng):
    size = rng.randint(0, 80)
    mode = rng.randrange(4)
    return [
        "(" * size
        if mode == 0
        else ")" * size
        if mode == 1
        else "()" * (size // 2)
        if mode == 2
        else "".join(rng.choice("()") for _ in range(size))
    ]
