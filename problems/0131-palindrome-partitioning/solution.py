class Solution:
    def partition(self, s: str) -> list[list[str]]:
        size = len(s)
        palindrome = [[False] * size for _ in range(size)]
        for start in range(size - 1, -1, -1):
            for end in range(start, size):
                palindrome[start][end] = s[start] == s[end] and (
                    end - start < 2 or palindrome[start + 1][end - 1]
                )
        answers = []
        path = []

        def split(start):
            if start == size:
                answers.append(path.copy())
                return
            for end in range(start, size):
                if palindrome[start][end]:
                    path.append(s[start : end + 1])
                    split(end + 1)
                    path.pop()

        split(0)
        return answers
