class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rows, cols = len(board), len(board[0])
        pending = []

        def protect(row, col):
            if board[row][col] == "O":
                board[row][col] = "#"
                pending.append((row, col))

        for row in range(rows):
            protect(row, 0)
            protect(row, cols - 1)
        for col in range(cols):
            protect(0, col)
            protect(rows - 1, col)
        while pending:
            row, col = pending.pop()
            for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if 0 <= nr < rows and 0 <= nc < cols:
                    protect(nr, nc)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "#":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
