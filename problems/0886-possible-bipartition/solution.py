from collections import deque


class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        adjacent = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            adjacent[a].append(b)
            adjacent[b].append(a)
        colors = [0] * (n + 1)
        for start in range(1, n + 1):
            if colors[start]:
                continue
            colors[start] = 1
            pending = deque([start])
            while pending:
                node = pending.popleft()
                for neighbor in adjacent[node]:
                    if colors[neighbor] == colors[node]:
                        return False
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        pending.append(neighbor)
        return True
