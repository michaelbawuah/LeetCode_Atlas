class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        escaped = set()
        pending = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] and (row in (0, rows - 1) or col in (0, cols - 1)):
                    escaped.add((row, col))
                    pending.append((row, col))
        while pending:
            r, c = pending.pop()
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] and (nr, nc) not in escaped:
                    escaped.add((nr, nc))
                    pending.append((nr, nc))
        return sum(grid[r][c] and (r, c) not in escaped for r in range(rows) for c in range(cols))
