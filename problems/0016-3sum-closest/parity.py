from itertools import combinations


def generate(rng):
    # The contract guarantees one closest sum; reject ties between different sums.
    while True:
        nums = [rng.randint(-1000, 1000) for _ in range(rng.randint(3, 20))]
        target = rng.randint(-10_000, 10_000)
        sums = {sum(group) for group in combinations(nums, 3)}
        distance = min(abs(total - target) for total in sums)
        if sum(abs(total - target) == distance for total in sums) == 1:
            return [nums, target]
