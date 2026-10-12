class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        best = [0] * (len(word2) + 1)
        for first in word1:
            diagonal = 0
            for column, second in enumerate(word2, start=1):
                above = best[column]
                best[column] = (
                    diagonal + 1 if first == second else max(best[column], best[column - 1])
                )
                diagonal = above
        return len(word1) + len(word2) - 2 * best[-1]
