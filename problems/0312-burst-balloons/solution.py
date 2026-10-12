class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        values = [1] + nums + [1]
        size = len(nums)
        best = [[0] * (size + 2) for _ in range(size + 2)]
        for length in range(1, size + 1):
            for left in range(1, size - length + 2):
                right = left + length - 1
                best[left][right] = max(
                    best[left][last - 1]
                    + values[left - 1] * values[last] * values[right + 1]
                    + best[last + 1][right]
                    for last in range(left, right + 1)
                )
        return best[1][size]
