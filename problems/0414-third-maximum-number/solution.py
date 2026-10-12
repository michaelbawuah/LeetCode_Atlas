class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first = second = third = None
        for value in nums:
            if value in (first, second, third):
                continue
            if first is None or value > first:
                first, second, third = value, first, second
            elif second is None or value > second:
                second, third = value, second
            elif third is None or value > third:
                third = value
        return first if third is None else third
