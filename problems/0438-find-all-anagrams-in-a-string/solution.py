from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        wanted, window = [0] * 26, [0] * 26
        for letter in p:
            wanted[ord(letter) - 97] += 1
        result = []
        for index, letter in enumerate(s):
            window[ord(letter) - 97] += 1
            if index >= len(p):
                window[ord(s[index - len(p)]) - 97] -= 1
            if index + 1 >= len(p) and window == wanted:
                result.append(index - len(p) + 1)
        return result
