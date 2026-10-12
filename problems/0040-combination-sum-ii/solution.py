class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ordered = sorted(candidates)
        answers = []
        path = []

        def choose(start, remaining):
            if remaining == 0:
                answers.append(path.copy())
                return
            for index in range(start, len(ordered)):
                value = ordered[index]
                if value > remaining:
                    break
                if index > start and value == ordered[index - 1]:
                    continue
                path.append(value)
                choose(index + 1, remaining - value)
                path.pop()

        choose(0, target)
        return answers
