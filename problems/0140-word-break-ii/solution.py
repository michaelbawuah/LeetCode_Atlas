class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        words = set(wordDict)
        longest = max(map(len, words))
        possible = [False] * len(s) + [True]
        for start in range(len(s) - 1, -1, -1):
            for end in range(start + 1, min(len(s), start + longest) + 1):
                if possible[end] and s[start:end] in words:
                    possible[start] = True
                    break
        sentences = []
        path = []

        def build(start):
            if start == len(s):
                sentences.append(" ".join(path))
                return
            for end in range(start + 1, min(len(s), start + longest) + 1):
                word = s[start:end]
                if possible[end] and word in words:
                    path.append(word)
                    build(end)
                    path.pop()

        if possible[0]:
            build(0)
        return sentences
