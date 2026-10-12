from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        counts = Counter(hand)
        for start in sorted(counts):
            groups = counts[start]
            if groups == 0:
                continue
            for value in range(start, start + groupSize):
                if counts[value] < groups:
                    return False
                counts[value] -= groups
        return True
