from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        finish = n * n
        pending = deque([(1, 0)])
        seen = {1}
        while pending:
            node, rolls = pending.popleft()
            if node == finish:
                return rolls
            for following in range(node + 1, min(finish, node + 6) + 1):
                row_from_bottom, col = divmod(following - 1, n)
                row = n - 1 - row_from_bottom
                if row_from_bottom % 2:
                    col = n - 1 - col
                destination = board[row][col] if board[row][col] != -1 else following
                if destination not in seen:
                    seen.add(destination)
                    pending.append((destination, rolls + 1))
        return -1
