from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        distances = [[-1] * cols for _ in range(rows)]
        pending = deque()
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    distances[row][col] = 0
                    pending.append((row, col))
        while pending:
            row, col = pending.popleft()
            for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if 0 <= nr < rows and 0 <= nc < cols and distances[nr][nc] == -1:
                    distances[nr][nc] = distances[row][col] + 1
                    pending.append((nr, nc))
        return distances
