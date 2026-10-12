from itertools import combinations


def generate(rng):
    while True:
        numbers = sorted(rng.randint(-1000, 1000) for _ in range(rng.randint(2, 30)))
        first, second = rng.sample(range(len(numbers)), 2)
        target = numbers[first] + numbers[second]
        if (
            -1000 <= target <= 1000
            and sum(
                numbers[left] + numbers[right] == target
                for left, right in combinations(range(len(numbers)), 2)
            )
            == 1
        ):
            return [numbers, target]
