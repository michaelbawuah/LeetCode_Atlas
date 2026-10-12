class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        while s[index] == " ":
            index -= 1
        end = index
        while index >= 0 and s[index] != " ":
            index -= 1
        return end - index
