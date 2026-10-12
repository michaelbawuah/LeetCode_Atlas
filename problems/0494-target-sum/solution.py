class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        ways = {0: 1}
        for value in nums:
            following: dict[int, int] = {}
            for subtotal, count in ways.items():
                positive, negative = subtotal + value, subtotal - value
                following[positive] = following.get(positive, 0) + count
                following[negative] = following.get(negative, 0) + count
            ways = following
        return ways.get(target, 0)
