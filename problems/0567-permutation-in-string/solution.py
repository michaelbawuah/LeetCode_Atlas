class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        width = len(s1)
        if width > len(s2):
            return False
        required = [0] * 26
        window = [0] * 26
        for char in s1:
            required[ord(char) - ord("a")] += 1
        for right, char in enumerate(s2):
            window[ord(char) - ord("a")] += 1
            if right >= width:
                window[ord(s2[right - width]) - ord("a")] -= 1
            if right >= width - 1 and window == required:
                return True
        return False
