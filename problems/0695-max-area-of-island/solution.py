class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        largest = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 1:
                    continue
                grid[row][col] = 0
                stack = [(row, col)]
                area = 0
                while stack:
                    current_row, current_col = stack.pop()
                    area += 1
                    for nr, nc in (
                        (current_row - 1, current_col),
                        (current_row + 1, current_col),
                        (current_row, current_col - 1),
                        (current_row, current_col + 1),
                    ):
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            stack.append((nr, nc))
                largest = max(largest, area)
        return largest
