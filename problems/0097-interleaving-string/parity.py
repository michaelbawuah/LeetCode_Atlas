def generate(rng):
    first, second = ["".join(rng.choices("abc", k=rng.randint(0, 25))) for _ in range(2)]
    if rng.random() < 0.5:
        one = two = 0
        merged = []
        while one < len(first) or two < len(second):
            if two == len(second) or (one < len(first) and rng.random() < 0.5):
                merged.append(first[one])
                one += 1
            else:
                merged.append(second[two])
                two += 1
        target = "".join(merged)
    else:
        target = "".join(rng.choices("abc", k=rng.randint(0, 50)))
    return [first, second, target]
