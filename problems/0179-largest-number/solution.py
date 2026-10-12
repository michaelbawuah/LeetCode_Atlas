from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(first: str, second: str) -> int:
            forward, backward = first + second, second + first
            return (backward > forward) - (backward < forward)

        values = sorted(map(str, nums), key=cmp_to_key(compare))
        return "0" if values[0] == "0" else "".join(values)
