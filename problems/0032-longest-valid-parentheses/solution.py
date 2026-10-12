class Solution:
    def longestValidParentheses(self, s: str) -> int:
        boundaries = [-1]
        best = 0
        for index, character in enumerate(s):
            if character == "(":
                boundaries.append(index)
            else:
                boundaries.pop()
                if not boundaries:
                    boundaries.append(index)
                else:
                    best = max(best, index - boundaries[-1])
        return best
