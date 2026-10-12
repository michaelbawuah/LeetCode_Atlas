class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        lengths = sorted({len(word) for word in words})
        possible = [True] + [False] * len(s)
        for end in range(1, len(s) + 1):
            for length in lengths:
                if length > end:
                    break
                if possible[end - length] and s[end - length : end] in words:
                    possible[end] = True
                    break
        return possible[-1]
