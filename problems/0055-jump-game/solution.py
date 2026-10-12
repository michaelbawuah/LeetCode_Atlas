class Solution:
    def canJump(self, nums: list[int]) -> bool:
        furthest = 0
        for index, reach in enumerate(nums):
            if index > furthest:
                return False
            furthest = max(furthest, index + reach)
            if furthest >= len(nums) - 1:
                return True
        return True
