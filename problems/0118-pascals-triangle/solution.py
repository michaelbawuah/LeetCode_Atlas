class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result: list[list[int]] = []
        for length in range(1, numRows + 1):
            row = [1] * length
            if result:
                for column in range(1, length - 1):
                    row[column] = result[-1][column - 1] + result[-1][column]
            result.append(row)
        return result
