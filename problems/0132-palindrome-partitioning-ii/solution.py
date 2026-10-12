class Solution:
    def minCut(self, s: str) -> int:
        cuts = list(range(-1, len(s)))
        for center in range(len(s)):
            for left, right in ((center, center), (center, center + 1)):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    cuts[right + 1] = min(cuts[right + 1], cuts[left] + 1)
                    left -= 1
                    right += 1
        return cuts[-1]
