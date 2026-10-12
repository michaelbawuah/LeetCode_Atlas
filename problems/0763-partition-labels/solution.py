class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {character: index for index, character in enumerate(s)}
        lengths = []
        start = end = 0
        for index, character in enumerate(s):
            end = max(end, last[character])
            if index == end:
                lengths.append(end - start + 1)
                start = index + 1
        return lengths
