from collections import Counter
from functools import cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def matches(first, second, length):
            left = s1[first : first + length]
            right = s2[second : second + length]
            if left == right:
                return True
            if Counter(left) != Counter(right):
                return False
            for cut in range(1, length):
                if matches(first, second, cut) and matches(first + cut, second + cut, length - cut):
                    return True
                if matches(first, second + length - cut, cut) and matches(
                    first + cut, second, length - cut
                ):
                    return True
            return False

        return matches(0, 0, len(s1))
