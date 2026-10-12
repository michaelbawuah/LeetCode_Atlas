from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        start = tuple(entrance)
        seen = {start}
        pending = deque([(start[0], start[1], 0)])
        while pending:
            row, col, distance = pending.popleft()
            for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and maze[nr][nc] == "."
                    and (nr, nc) not in seen
                ):
                    if nr in (0, rows - 1) or nc in (0, cols - 1):
                        return distance + 1
                    seen.add((nr, nc))
                    pending.append((nr, nc, distance + 1))
        return -1
