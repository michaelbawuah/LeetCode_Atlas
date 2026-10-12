from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n <= 2:
            return list(range(n))
        adjacent = [[] for _ in range(n)]
        for first, last in edges:
            adjacent[first].append(last)
            adjacent[last].append(first)
        degree = [len(neighbors) for neighbors in adjacent]
        leaves = deque(index for index, value in enumerate(degree) if value == 1)
        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                for neighbor in adjacent[node]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        return list(leaves)
