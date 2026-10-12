def generate(rng):
    nums = [rng.randint(0, 8) for _ in range(rng.randint(1, 12))]
    mode = rng.randrange(4)
    if mode == 0:
        nums.sort()
    elif mode == 1:
        nums.sort(reverse=True)
    elif mode == 2:
        nums = [nums[0]] * len(nums)
    return [nums]
