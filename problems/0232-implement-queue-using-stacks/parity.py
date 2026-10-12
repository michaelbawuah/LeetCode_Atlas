"""Valid seeded inputs for Python/C++ comparison."""


def generate(rng):
    operations, arguments = ["MyQueue"], [[]]
    size = 0
    for _ in range(rng.randint(1, 99)):
        operation = rng.choice(["push", "pop", "peek", "empty"] if size else ["push", "empty"])
        operations.append(operation)
        arguments.append([rng.randint(1, 9)] if operation == "push" else [])
        if operation == "push":
            size += 1
        elif operation == "pop":
            size -= 1
    return [operations, arguments]
