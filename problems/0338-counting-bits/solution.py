class Solution:
    def countBits(self, n: int) -> list[int]:
        counts = [0] * (n + 1)
        for value in range(1, n + 1):
            counts[value] = counts[value >> 1] + (value & 1)
        return counts
