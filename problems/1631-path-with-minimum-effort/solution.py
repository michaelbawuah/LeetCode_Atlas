from heapq import heappop, heappush


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        effort = [[float("inf")] * cols for _ in range(rows)]
        effort[0][0] = 0
        pending = [(0, 0, 0)]
        while pending:
            cost, row, col = heappop(pending)
            if cost != effort[row][col]:
                continue
            if row == rows - 1 and col == cols - 1:
                return cost
            for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if 0 <= nr < rows and 0 <= nc < cols:
                    following = max(cost, abs(heights[row][col] - heights[nr][nc]))
                    if following < effort[nr][nc]:
                        effort[nr][nc] = following
                        heappush(pending, (following, nr, nc))
        return 0
