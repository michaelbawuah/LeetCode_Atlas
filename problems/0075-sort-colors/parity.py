def generate(rng):
    nums = [rng.randrange(3) for _ in range(rng.randint(1, 80))]
    if rng.randrange(4) == 0:
        nums = [rng.randrange(3)] * len(nums)
    return [nums]
