from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])
        if len(word) > rows * columns:
            return False

        def visit(row, column, index):
            if (
                row < 0
                or row >= rows
                or column < 0
                or column >= columns
                or board[row][column] != word[index]
            ):
                return False
            if index + 1 == len(word):
                return True
            letter = board[row][column]
            board[row][column] = ""
            result = any(
                visit(row + dr, column + dc, index + 1)
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
            )
            board[row][column] = letter
            return result

        return any(visit(row, column, 0) for row in range(rows) for column in range(columns))
