from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups: dict[tuple[int, ...], list[str]] = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for character in word:
                counts[ord(character) - ord("a")] += 1
            groups[tuple(counts)].append(word)
        return list(groups.values())
