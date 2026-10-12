class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber:
            columnNumber, digit = divmod(columnNumber - 1, 26)
            result.append(chr(ord("A") + digit))
        return "".join(reversed(result))
