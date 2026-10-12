class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        previous = matrix[0].copy()
        for index in range(1, len(matrix)):
            row = matrix[index]
            previous = [
                value + min(previous[max(0, column - 1) : column + 2])
                for column, value in enumerate(row)
            ]
        return min(previous)
