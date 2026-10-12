from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != "1":
                    continue
                islands += 1
                grid[row][col] = "0"
                stack = [(row, col)]
                while stack:
                    current_row, current_col = stack.pop()
                    for next_row, next_col in (
                        (current_row - 1, current_col),
                        (current_row + 1, current_col),
                        (current_row, current_col - 1),
                        (current_row, current_col + 1),
                    ):
                        if (
                            0 <= next_row < rows
                            and 0 <= next_col < cols
                            and grid[next_row][next_col] == "1"
                        ):
                            grid[next_row][next_col] = "0"
                            stack.append((next_row, next_col))
        return islands
