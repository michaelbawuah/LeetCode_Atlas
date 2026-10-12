class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ordered = sorted(nums)
        answers = []
        path = []

        def choose(start):
            answers.append(path.copy())
            for index in range(start, len(ordered)):
                if index > start and ordered[index] == ordered[index - 1]:
                    continue
                path.append(ordered[index])
                choose(index + 1)
                path.pop()

        choose(0)
        return answers
