class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        answers = [[]]
        for value in nums:
            answers.extend([subset + [value] for subset in answers])
        return answers
