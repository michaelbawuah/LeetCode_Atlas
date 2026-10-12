from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if startGene == endGene:
            return 0
        available = set(bank)
        if endGene not in available:
            return -1
        pending = deque([(startGene, 0)])
        seen = {startGene}
        while pending:
            gene, steps = pending.popleft()
            for index in range(len(gene)):
                for letter in "ACGT":
                    following = gene[:index] + letter + gene[index + 1 :]
                    if following in available and following not in seen:
                        if following == endGene:
                            return steps + 1
                        seen.add(following)
                        pending.append((following, steps + 1))
        return -1
