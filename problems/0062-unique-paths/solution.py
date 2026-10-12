class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        width, height = min(m, n), max(m, n)
        paths = [1] * width
        for _ in range(1, height):
            for column in range(1, width):
                paths[column] += paths[column - 1]
        return paths[-1]
