class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        forward, backward = {}, {}
        for letter, word in zip(pattern, words, strict=True):
            if forward.get(letter, word) != word or backward.get(word, letter) != letter:
                return False
            forward[letter], backward[word] = word, letter
        return True
