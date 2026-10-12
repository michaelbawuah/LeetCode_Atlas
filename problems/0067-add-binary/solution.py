class Solution:
    def addBinary(self, a: str, b: str) -> str:
        left, right, carry = len(a) - 1, len(b) - 1, 0
        result = []
        while left >= 0 or right >= 0 or carry:
            total = carry
            if left >= 0:
                total += ord(a[left]) - ord("0")
                left -= 1
            if right >= 0:
                total += ord(b[right]) - ord("0")
                right -= 1
            result.append(str(total % 2))
            carry = total // 2
        return "".join(reversed(result))
