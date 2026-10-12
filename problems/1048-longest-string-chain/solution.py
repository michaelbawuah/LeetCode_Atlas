class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        best = {}
        for word in sorted(words, key=len):
            best[word] = max(
                1 + best.get(word[:index] + word[index + 1 :], 0) for index in range(len(word))
            )
        return max(best.values())
