class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        closed = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] or (row, col) in seen:
                    continue
                seen.add((row, col))
                pending = [(row, col)]
                touches = False
                while pending:
                    r, c = pending.pop()
                    touches |= r in (0, rows - 1) or c in (0, cols - 1)
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and not grid[nr][nc]
                            and (nr, nc) not in seen
                        ):
                            seen.add((nr, nc))
                            pending.append((nr, nc))
                closed += not touches
        return closed
