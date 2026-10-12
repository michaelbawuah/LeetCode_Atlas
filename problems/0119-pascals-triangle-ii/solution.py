class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for column in range(1, rowIndex + 1):
            row.append(row[-1] * (rowIndex - column + 1) // column)
        return row
