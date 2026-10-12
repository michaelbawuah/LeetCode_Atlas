from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                values.append(int(token))
                continue
            right = values.pop()
            left = values.pop()
            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            else:
                quotient = abs(left) // abs(right)
                result = -quotient if (left < 0) != (right < 0) else quotient
            values.append(result)
        return values[0]
