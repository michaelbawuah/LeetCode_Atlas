class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ending_here = best = nums[0]
        for index in range(1, len(nums)):
            ending_here = max(nums[index], ending_here + nums[index])
            best = max(best, ending_here)
        return best
