"""Valid seeded inputs for Python/C++ comparison."""


def generate(rng):
    boundary = rng.choice([2147483646, 2147483647, 2147483648, 2147483649, 99999999999999999999])
    if rng.randrange(3) == 0:
        return [
            " " * rng.randint(0, 5)
            + rng.choice(["", "+", "-"])
            + "0" * rng.randint(0, 8)
            + str(boundary)
            + rng.choice(["", "abc", " 12", ".0"])
        ]
    return ["".join(rng.choice(" 0123456789+-abc.") for _ in range(rng.randint(0, 80)))]
