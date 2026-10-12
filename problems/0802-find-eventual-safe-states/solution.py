from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        parents = [[] for _ in graph]
        degree = [len(neighbors) for neighbors in graph]
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                parents[neighbor].append(node)
        pending = deque(node for node, count in enumerate(degree) if count == 0)
        while pending:
            node = pending.popleft()
            for parent in parents[node]:
                degree[parent] -= 1
                if degree[parent] == 0:
                    pending.append(parent)
        return [node for node, count in enumerate(degree) if count == 0]
