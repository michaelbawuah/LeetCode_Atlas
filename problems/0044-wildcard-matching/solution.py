class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        previous = [True] + [False] * len(p)
        for column, token in enumerate(p, start=1):
            previous[column] = previous[column - 1] and token == "*"
        for character in s:
            current = [False] * (len(p) + 1)
            for column, token in enumerate(p, start=1):
                if token == "*":
                    current[column] = current[column - 1] or previous[column]
                else:
                    current[column] = previous[column - 1] and token in ("?", character)
            previous = current
        return previous[-1]
