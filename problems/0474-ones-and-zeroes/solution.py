class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        best = [[0] * (n + 1) for _ in range(m + 1)]
        for word in strs:
            zeros = word.count("0")
            ones = len(word) - zeros
            for zero_budget in range(m, zeros - 1, -1):
                for one_budget in range(n, ones - 1, -1):
                    best[zero_budget][one_budget] = max(
                        best[zero_budget][one_budget],
                        1 + best[zero_budget - zeros][one_budget - ones],
                    )
        return best[m][n]
