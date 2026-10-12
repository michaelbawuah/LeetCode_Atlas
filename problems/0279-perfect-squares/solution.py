from math import isqrt


class Solution:
    def numSquares(self, n: int) -> int:
        squares = [value * value for value in range(1, isqrt(n) + 1)]
        best = [0] + [n + 1] * n
        for total in range(1, n + 1):
            for square in squares:
                if square > total:
                    break
                best[total] = min(best[total], best[total - square] + 1)
        return best[n]
