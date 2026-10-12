class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        previous = list(range(len(word2) + 1))
        for row, first in enumerate(word1, start=1):
            current = [row] + [0] * len(word2)
            for column, second in enumerate(word2, start=1):
                if first == second:
                    current[column] = previous[column - 1]
                else:
                    current[column] = 1 + min(
                        previous[column], current[column - 1], previous[column - 1]
                    )
            previous = current
        return previous[-1]
