class Solution:
    def countAndSay(self, n: int) -> str:
        term = "1"
        for _ in range(n - 1):
            pieces = []
            start = 0
            while start < len(term):
                end = start + 1
                while end < len(term) and term[end] == term[start]:
                    end += 1
                pieces.extend((str(end - start), term[start]))
                start = end
            term = "".join(pieces)
        return term
