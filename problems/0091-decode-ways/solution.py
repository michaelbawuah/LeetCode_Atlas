class Solution:
    def numDecodings(self, s: str) -> int:
        two_back = 1
        one_back = int(s[0] != "0")
        for index in range(1, len(s)):
            ways = one_back if s[index] != "0" else 0
            if 10 <= int(s[index - 1 : index + 1]) <= 26:
                ways += two_back
            two_back, one_back = one_back, ways
        return one_back
