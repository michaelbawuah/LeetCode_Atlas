from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node["#"] = word
        rows, columns = len(board), len(board[0])
        found = []

        def visit(row, column, parent):
            letter = board[row][column]
            if letter not in parent:
                return
            node = parent[letter]
            word = node.pop("#", None)
            if word is not None:
                found.append(word)
            board[row][column] = ""
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, column + dc
                if 0 <= nr < rows and 0 <= nc < columns and board[nr][nc] in node:
                    visit(nr, nc, node)
            board[row][column] = letter
            if not node:
                del parent[letter]

        for row in range(rows):
            for column in range(columns):
                visit(row, column, trie)
        return found
