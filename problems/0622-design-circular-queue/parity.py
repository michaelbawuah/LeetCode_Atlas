"""Generate valid inputs for reproducible cross-language comparisons."""


def generate(rng):
    operations = ["MyCircularQueue"]
    arguments = [[rng.randint(1, 8)]]
    for _ in range(100):
        operation = rng.choice(["enQueue", "deQueue", "Front", "Rear", "isEmpty", "isFull"])
        operations.append(operation)
        arguments.append([rng.randint(0, 1000)] if operation == "enQueue" else [])
    return [operations, arguments]
