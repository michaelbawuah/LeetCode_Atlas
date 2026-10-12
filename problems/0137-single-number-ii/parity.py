def generate(rng):
    values = rng.sample(list(range(-30, 31)) + [-2147483648, 2147483647], rng.randint(1, 8))
    singleton = rng.choice(values)
    nums = [singleton] + [value for value in values if value != singleton for _ in range(3)]
    rng.shuffle(nums)
    return [nums]
