class Solution:
    def isValid(self, s: str) -> bool:
        matches = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            elif not stack or stack.pop() != matches[char]:
                return False
        return not stack
