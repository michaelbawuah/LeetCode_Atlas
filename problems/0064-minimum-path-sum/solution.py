class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        best = [0] + [float("inf")] * (len(grid[0]) - 1)
        for row in grid:
            for column, cost in enumerate(row):
                if column == 0:
                    best[column] += cost
                else:
                    best[column] = min(best[column], best[column - 1]) + cost
        return best[-1]
