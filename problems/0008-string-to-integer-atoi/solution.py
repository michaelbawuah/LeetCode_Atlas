class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        while index < len(s) and s[index] == " ":
            index += 1
        sign = 1
        if index < len(s) and s[index] in "+-":
            sign = -1 if s[index] == "-" else 1
            index += 1
        result = 0
        while index < len(s) and "0" <= s[index] <= "9":
            result = result * 10 + ord(s[index]) - ord("0")
            index += 1
            if sign * result < -(2**31):
                return -(2**31)
            if sign * result > 2**31 - 1:
                return 2**31 - 1
        return sign * result
