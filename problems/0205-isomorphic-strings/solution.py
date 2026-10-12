class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        forward, backward = {}, {}
        for first, second in zip(s, t, strict=True):
            if forward.get(first, second) != second or backward.get(second, first) != first:
                return False
            forward[first], backward[second] = second, first
        return True
