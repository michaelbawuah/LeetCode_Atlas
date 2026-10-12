class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        previous = [0]
        for character in s2:
            previous.append(previous[-1] + ord(character))
        for first in s1:
            current = [previous[0] + ord(first)] + [0] * len(s2)
            for column, second in enumerate(s2, start=1):
                current[column] = (
                    previous[column - 1]
                    if first == second
                    else min(previous[column] + ord(first), current[column - 1] + ord(second))
                )
            previous = current
        return previous[-1]
