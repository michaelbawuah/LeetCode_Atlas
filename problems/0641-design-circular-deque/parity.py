"""Valid seeded inputs for Python/C++ comparison."""


def generate(rng):
    capacity = rng.choice([1, 2, rng.randint(1, 10)])
    operations, arguments = ["MyCircularDeque"], [[capacity]]
    choices = [
        "insertFront",
        "insertLast",
        "deleteFront",
        "deleteLast",
        "getFront",
        "getRear",
        "isEmpty",
        "isFull",
    ]
    for _ in range(rng.randint(1, 100)):
        operation = rng.choice(choices)
        operations.append(operation)
        arguments.append([rng.randint(0, 1000)] if operation.startswith("insert") else [])
    return [operations, arguments]
