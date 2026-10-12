"""Valid seeded inputs for Python/C++ comparison."""


def generate(rng):
    operations, arguments = ["MyCalendar"], [[]]
    previous = []
    for _ in range(rng.randint(1, 100)):
        if previous and rng.randrange(4) == 0:
            start, end = rng.choice(previous)
            if rng.randrange(2) == 0 and end < 1000000000:
                start, end = end, min(1000000000, end + rng.randint(1, 30))
        else:
            start = rng.choice([0, 999999999, rng.randint(0, 200)])
            end = min(1000000000, start + rng.randint(1, 30))
        operations.append("book")
        arguments.append([start, end])
        previous.append((start, end))
    return [operations, arguments]
