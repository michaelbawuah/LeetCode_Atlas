class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        answer = len(nums)
        for index, value in enumerate(nums):
            answer ^= index ^ value
        return answer
