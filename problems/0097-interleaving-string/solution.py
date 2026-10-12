class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        possible = [True] + [False] * len(s2)
        for column in range(1, len(s2) + 1):
            possible[column] = possible[column - 1] and s2[column - 1] == s3[column - 1]
        for row in range(1, len(s1) + 1):
            possible[0] = possible[0] and s1[row - 1] == s3[row - 1]
            for column in range(1, len(s2) + 1):
                newest = s3[row + column - 1]
                possible[column] = (possible[column] and s1[row - 1] == newest) or (
                    possible[column - 1] and s2[column - 1] == newest
                )
        return possible[-1]
