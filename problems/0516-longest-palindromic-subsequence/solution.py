class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        best = [0] * len(s)
        for left in range(len(s) - 1, -1, -1):
            best[left] = 1
            diagonal = 0
            for right in range(left + 1, len(s)):
                above = best[right]
                if s[left] == s[right]:
                    best[right] = diagonal + 2
                else:
                    best[right] = max(best[right], best[right - 1])
                diagonal = above
        return best[-1]
