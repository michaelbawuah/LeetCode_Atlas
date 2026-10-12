class _Node:
    def __init__(self):
        self.children = {}
        self.terminal = False


class Trie:
    def __init__(self):
        self._root = _Node()

    def insert(self, word: str) -> None:
        node = self._root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = _Node()
            node = node.children[letter]
        node.terminal = True

    def _walk(self, text: str):
        node = self._root
        for letter in text:
            node = node.children.get(letter)
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.terminal

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None
