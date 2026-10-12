from itertools import product


def generate(rng):
    width = rng.randint(1, 3)
    universe = ["".join(chars) for chars in product("abc", repeat=width)]
    begin, end = rng.sample(universe, 2)
    words = rng.sample(universe, rng.randint(1, min(20, len(universe))))
    return [begin, end, words]
