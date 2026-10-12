from collections import deque


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        distances = [[-1] * n for _ in range(n)]
        pending = deque()
        for row in range(n):
            for col in range(n):
                if grid[row][col]:
                    distances[row][col] = 0
                    pending.append((row, col))
        if not pending or len(pending) == n * n:
            return -1
        farthest = 0
        while pending:
            row, col = pending.popleft()
            for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if 0 <= nr < n and 0 <= nc < n and distances[nr][nc] == -1:
                    distances[nr][nc] = distances[row][col] + 1
                    farthest = max(farthest, distances[nr][nc])
                    pending.append((nr, nc))
        return farthest
