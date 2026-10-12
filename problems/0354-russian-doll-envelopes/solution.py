from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        tails = []
        for _, height in sorted(envelopes, key=lambda pair: (pair[0], -pair[1])):
            position = bisect_left(tails, height)
            if position == len(tails):
                tails.append(height)
            else:
                tails[position] = height
        return len(tails)
