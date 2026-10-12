from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        adjacent = defaultdict(list)
        for (first, last), value in zip(equations, values, strict=True):
            adjacent[first].append((last, value))
            adjacent[last].append((first, 1.0 / value))
        answers = []
        for first, last in queries:
            if first not in adjacent or last not in adjacent:
                answers.append(-1.0)
                continue
            seen, pending = {first}, [(first, 1.0)]
            answer = -1.0
            while pending:
                node, product = pending.pop()
                if node == last:
                    answer = product
                    break
                for neighbor, ratio in adjacent[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        pending.append((neighbor, product * ratio))
            answers.append(answer)
        return answers
