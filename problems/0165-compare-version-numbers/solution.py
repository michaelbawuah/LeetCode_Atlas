class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        first, second = version1.split("."), version2.split(".")
        for index in range(max(len(first), len(second))):
            a = int(first[index]) if index < len(first) else 0
            b = int(second[index]) if index < len(second) else 0
            if a != b:
                return 1 if a > b else -1
        return 0
