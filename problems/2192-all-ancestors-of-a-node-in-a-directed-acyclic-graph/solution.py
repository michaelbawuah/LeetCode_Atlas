from collections import deque


class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        adjacent = [[] for _ in range(n)]
        degree = [0] * n
        for first, last in edges:
            adjacent[first].append(last)
            degree[last] += 1
        ancestors = [set() for _ in range(n)]
        pending = deque(node for node, count in enumerate(degree) if count == 0)
        while pending:
            node = pending.popleft()
            for neighbor in adjacent[node]:
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    pending.append(neighbor)
        return [sorted(values) for values in ancestors]
