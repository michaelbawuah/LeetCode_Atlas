class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        sides = [0] * (len(matrix[0]) + 1)
        largest = 0
        for row in matrix:
            diagonal = 0
            for column, value in enumerate(row, start=1):
                above = sides[column]
                if value == "1":
                    sides[column] = 1 + min(sides[column], sides[column - 1], diagonal)
                    largest = max(largest, sides[column])
                else:
                    sides[column] = 0
                diagonal = above
        return largest * largest
