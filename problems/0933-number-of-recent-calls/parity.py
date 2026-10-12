"""Generate valid inputs for reproducible cross-language comparisons."""


def generate(rng):
    time = 0
    arguments = [[]]
    for _ in range(rng.randint(1, 100)):
        time += rng.choice([1, 3000, 3001, rng.randint(1, 5000)])
        arguments.append([time])
    return [["RecentCounter"] + ["ping"] * (len(arguments) - 1), arguments]
