from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = Counter(t)
        missing = len(t)
        left = 0
        best_start, best_length = 0, len(s) + 1
        for right, character in enumerate(s):
            if required[character] > 0:
                missing -= 1
            required[character] -= 1
            while missing == 0:
                length = right - left + 1
                if length < best_length:
                    best_start, best_length = left, length
                departing = s[left]
                required[departing] += 1
                if required[departing] > 0:
                    missing += 1
                left += 1
        if best_length > len(s):
            return ""
        return s[best_start : best_start + best_length]
