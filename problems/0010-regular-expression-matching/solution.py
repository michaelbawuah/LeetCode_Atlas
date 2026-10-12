class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        previous = [False] * (len(p) + 1)
        previous[0] = True
        for column in range(2, len(p) + 1):
            if p[column - 1] == "*":
                previous[column] = previous[column - 2]
        for letter in s:
            current = [False] * (len(p) + 1)
            for column in range(1, len(p) + 1):
                atom = p[column - 1]
                if atom == "*":
                    matches = p[column - 2] in {".", letter}
                    current[column] = current[column - 2] or (matches and previous[column])
                else:
                    current[column] = previous[column - 1] and atom in {".", letter}
            previous = current
        return previous[-1]
