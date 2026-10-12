from collections import Counter


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        counts = Counter(nums)
        choices = sorted(counts)
        answers = []
        path = []

        def arrange():
            if len(path) == len(nums):
                answers.append(path.copy())
                return
            for value in choices:
                if counts[value] == 0:
                    continue
                counts[value] -= 1
                path.append(value)
                arrange()
                path.pop()
                counts[value] += 1

        arrange()
        return answers
