from collections import deque


class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        start = next((r, c) for r in range(n) for c in range(n) if grid[r][c])
        island = {start}
        pending = [start]
        while pending:
            row, col = pending.pop()
            for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] and (nr, nc) not in island:
                    island.add((nr, nc))
                    pending.append((nr, nc))
        seen = set(island)
        wave = deque((r, c, 0) for r, c in island)
        while wave:
            row, col, distance = wave.popleft()
            for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                    if grid[nr][nc]:
                        return distance
                    seen.add((nr, nc))
                    wave.append((nr, nc, distance + 1))
        return -1
