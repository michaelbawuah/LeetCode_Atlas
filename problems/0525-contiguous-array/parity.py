def generate(rng):
    nums = [rng.randrange(2) for _ in range(rng.randint(1, 80))]
    if rng.randrange(5) == 0:
        nums = [rng.randrange(2)] * len(nums)
    return [nums]
