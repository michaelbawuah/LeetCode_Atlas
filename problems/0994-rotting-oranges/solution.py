from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        minutes = 0
        while rotten and fresh:
            for _ in range(len(rotten)):
                row, col = rotten.popleft()
                for next_row, next_col in (
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ):
                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and grid[next_row][next_col] == 1
                    ):
                        grid[next_row][next_col] = 2
                        fresh -= 1
                        rotten.append((next_row, next_col))
            minutes += 1
        return minutes if fresh == 0 else -1
