class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        failure = [0] * len(needle)
        for index in range(1, len(needle)):
            matched = failure[index - 1]
            while matched and needle[index] != needle[matched]:
                matched = failure[matched - 1]
            if needle[index] == needle[matched]:
                matched += 1
            failure[index] = matched
        matched = 0
        for index, letter in enumerate(haystack):
            while matched and letter != needle[matched]:
                matched = failure[matched - 1]
            if letter == needle[matched]:
                matched += 1
            if matched == len(needle):
                return index - len(needle) + 1
        return -1
