from collections import deque


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        degree = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                degree[row][col] = sum(
                    0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[row][col]
                    for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1))
                )
        pending = deque(
            (row, col) for row in range(rows) for col in range(cols) if degree[row][col] == 0
        )
        length = 0
        while pending:
            length += 1
            for _ in range(len(pending)):
                row, col = pending.popleft()
                for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] < matrix[row][col]:
                        degree[nr][nc] -= 1
                        if degree[nr][nc] == 0:
                            pending.append((nr, nc))
        return length
