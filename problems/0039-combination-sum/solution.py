class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        choices = sorted(candidates)
        answers = []
        path = []

        def search(start, remaining):
            if remaining == 0:
                answers.append(path.copy())
                return
            for index in range(start, len(choices)):
                value = choices[index]
                if value > remaining:
                    break
                path.append(value)
                search(index, remaining - value)
                path.pop()

        search(0, target)
        return answers
