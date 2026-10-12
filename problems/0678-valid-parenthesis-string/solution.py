class Solution:
    def checkValidString(self, s: str) -> bool:
        minimum = maximum = 0
        for character in s:
            if character == "(":
                minimum += 1
                maximum += 1
            elif character == ")":
                minimum -= 1
                maximum -= 1
            else:
                minimum -= 1
                maximum += 1
            if maximum < 0:
                return False
            minimum = max(minimum, 0)
        return minimum == 0
