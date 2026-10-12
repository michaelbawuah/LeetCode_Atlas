"""Valid seeded inputs for Python/C++ comparison."""


def generate(rng):
    operations, arguments = ["WordDictionary"], [[]]
    inserted = []
    for _ in range(rng.randint(1, 70)):
        word = "".join(rng.choice("abcxyz") for _ in range(rng.randint(1, 25)))
        if rng.randrange(5) < 2:
            if inserted and rng.randrange(4) == 0:
                word = rng.choice(inserted)
            operations.append("addWord")
            arguments.append([word])
            inserted.append(word)
        else:
            if inserted and rng.randrange(2) == 0:
                word = rng.choice(inserted)
            wildcard = set(rng.sample(range(len(word)), rng.randint(0, min(2, len(word)))))
            pattern = "".join(
                "." if index in wildcard else letter for index, letter in enumerate(word)
            )
            operations.append("search")
            arguments.append([pattern])
    return [operations, arguments]
