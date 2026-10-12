def generate(rng):
    n = rng.randint(1, 30)
    duplicate = rng.randint(1, n)
    copies = rng.randint(2, n + 1)
    others = rng.sample([value for value in range(1, n + 1) if value != duplicate], n + 1 - copies)
    nums = [duplicate] * copies + others
    rng.shuffle(nums)
    return [nums]
