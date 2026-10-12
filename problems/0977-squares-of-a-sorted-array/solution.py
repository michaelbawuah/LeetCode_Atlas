class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1
        for write in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[write] = nums[left] * nums[left]
                left += 1
            else:
                result[write] = nums[right] * nums[right]
                right -= 1
        return result
