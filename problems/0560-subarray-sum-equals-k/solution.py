class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        frequencies = {0: 1}
        prefix = answer = 0
        for value in nums:
            prefix += value
            answer += frequencies.get(prefix - k, 0)
            frequencies[prefix] = frequencies.get(prefix, 0) + 1
        return answer
