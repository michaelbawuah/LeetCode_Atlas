class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for value in nums:
            index = abs(value) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        return [index + 1 for index, value in enumerate(nums) if value > 0]
