class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [[] for _ in range(numRows)]
        row, direction = 0, 1
        for letter in s:
            rows[row].append(letter)
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1
            row += direction
        return "".join("".join(values) for values in rows)
