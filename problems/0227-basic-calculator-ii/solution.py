class Solution:
    def calculate(self, s: str) -> int:
        terms = []
        number, operation = 0, "+"
        for letter in s + "+":
            if "0" <= letter <= "9":
                number = number * 10 + ord(letter) - ord("0")
            elif letter != " ":
                if operation == "+":
                    terms.append(number)
                elif operation == "-":
                    terms.append(-number)
                elif operation == "*":
                    terms[-1] *= number
                else:
                    quotient = abs(terms[-1]) // number
                    terms[-1] = -quotient if terms[-1] < 0 else quotient
                operation, number = letter, 0
        return sum(terms)
