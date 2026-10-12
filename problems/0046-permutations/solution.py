class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        values = nums.copy()
        answers = []

        def arrange(start):
            if start == len(values):
                answers.append(values.copy())
                return
            for index in range(start, len(values)):
                values[start], values[index] = values[index], values[start]
                arrange(start + 1)
                values[start], values[index] = values[index], values[start]

        arrange(0)
        return answers
