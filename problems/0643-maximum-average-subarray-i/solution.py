class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total = sum(nums[index] for index in range(k))
        best = total
        for right in range(k, len(nums)):
            total += nums[right] - nums[right - k]
            best = max(best, total)
        return best / k
