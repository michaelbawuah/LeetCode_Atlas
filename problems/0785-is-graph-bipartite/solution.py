from collections import deque


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        colors = [0] * len(graph)
        for start in range(len(graph)):
            if colors[start]:
                continue
            colors[start] = 1
            pending = deque([start])
            while pending:
                node = pending.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == colors[node]:
                        return False
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        pending.append(neighbor)
        return True
