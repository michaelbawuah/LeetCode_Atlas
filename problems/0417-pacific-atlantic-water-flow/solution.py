class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])

        def reachable(starts):
            seen = set(starts)
            stack = list(seen)
            while stack:
                row, col = stack.pop()
                for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in seen
                        and heights[nr][nc] >= heights[row][col]
                    ):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            return seen

        pacific = reachable([(row, 0) for row in range(rows)] + [(0, col) for col in range(cols)])
        atlantic = reachable(
            [(row, cols - 1) for row in range(rows)] + [(rows - 1, col) for col in range(cols)]
        )
        return [
            [row, col]
            for row in range(rows)
            for col in range(cols)
            if (row, col) in pacific and (row, col) in atlantic
        ]
