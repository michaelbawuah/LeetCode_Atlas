from collections import deque


class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        adjacent = [[] for _ in range(n)]
        degree = [0] * n
        for first, last in relations:
            adjacent[first - 1].append(last - 1)
            degree[last - 1] += 1
        completed = time.copy()
        pending = deque(node for node, count in enumerate(degree) if count == 0)
        while pending:
            node = pending.popleft()
            for neighbor in adjacent[node]:
                completed[neighbor] = max(completed[neighbor], completed[node] + time[neighbor])
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    pending.append(neighbor)
        return max(completed)
