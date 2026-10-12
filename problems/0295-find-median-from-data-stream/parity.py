"""Valid seeded inputs for Python/C++ comparison."""


def generate(rng):
    operations, arguments = ["MedianFinder", "addNum"], [[], [rng.randint(-100000, 100000)]]
    for _ in range(rng.randint(1, 80)):
        operation = rng.choice(["addNum", "findMedian", "findMedian"])
        operations.append(operation)
        arguments.append(
            [rng.choice([-100000, 100000, rng.randint(-100000, 100000)])]
            if operation == "addNum"
            else []
        )
    return [operations, arguments]
