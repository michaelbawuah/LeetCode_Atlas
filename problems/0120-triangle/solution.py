class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        best = triangle[-1].copy()
        for row in range(len(triangle) - 2, -1, -1):
            for column, value in enumerate(triangle[row]):
                best[column] = value + min(best[column], best[column + 1])
        return best[0]
