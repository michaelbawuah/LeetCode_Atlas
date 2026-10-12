class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        remaining = abs(x)
        result = 0
        limit = 2**31 if negative else 2**31 - 1
        while remaining:
            remaining, digit = divmod(remaining, 10)
            if result > (limit - digit) // 10:
                return 0
            result = result * 10 + digit
        return -result if negative else result
