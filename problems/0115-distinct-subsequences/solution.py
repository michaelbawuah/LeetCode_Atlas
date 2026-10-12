class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        counts = [1] + [0] * len(t)
        for first in s:
            for length in range(len(t), 0, -1):
                if first == t[length - 1]:
                    counts[length] += counts[length - 1]
        return counts[-1]
