class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        answers = []
        path = []

        def extend(opened, closed):
            if closed == n:
                answers.append("".join(path))
                return
            if opened < n:
                path.append("(")
                extend(opened + 1, closed)
                path.pop()
            if closed < opened:
                path.append(")")
                extend(opened, closed + 1)
                path.pop()

        extend(0, 0)
        return answers
