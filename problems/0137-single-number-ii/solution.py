class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        once = twice = 0
        for value in nums:
            once = (once ^ value) & ~twice
            twice = (twice ^ value) & ~once
        return once
