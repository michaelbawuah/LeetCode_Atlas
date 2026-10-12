from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        counts = Counter(nums)
        previous = None
        two_back = one_back = 0
        for value in sorted(counts):
            earned = value * counts[value]
            following = (
                max(one_back, two_back + earned)
                if previous is not None and value == previous + 1
                else one_back + earned
            )
            two_back, one_back, previous = one_back, following, value
        return one_back
