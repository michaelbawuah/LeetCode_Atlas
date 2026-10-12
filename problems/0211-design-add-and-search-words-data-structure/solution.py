class _Node:
    def __init__(self):
        self.children = {}
        self.terminal = False


class WordDictionary:
    def __init__(self):
        self._root = _Node()

    def addWord(self, word: str) -> None:
        node = self._root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = _Node()
            node = node.children[letter]
        node.terminal = True

    def search(self, word: str) -> bool:
        frontier = [self._root]
        for letter in word:
            following = []
            for node in frontier:
                if letter == ".":
                    following.extend(node.children.values())
                elif letter in node.children:
                    following.append(node.children[letter])
            if not following:
                return False
            frontier = following
        return any(node.terminal for node in frontier)
