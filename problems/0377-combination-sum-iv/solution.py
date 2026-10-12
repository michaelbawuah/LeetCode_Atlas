class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        counts = [1] + [0] * target
        for total in range(1, target + 1):
            counts[total] = sum(counts[total - value] for value in nums if value <= total)
        return counts[target]
