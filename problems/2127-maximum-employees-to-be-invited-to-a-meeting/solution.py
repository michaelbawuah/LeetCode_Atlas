from collections import deque


class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        n = len(favorite)
        degree = [0] * n
        for node in favorite:
            degree[node] += 1
        depth = [1] * n
        pending = deque(node for node, count in enumerate(degree) if count == 0)
        while pending:
            node = pending.popleft()
            neighbor = favorite[node]
            depth[neighbor] = max(depth[neighbor], depth[node] + 1)
            degree[neighbor] -= 1
            if degree[neighbor] == 0:
                pending.append(neighbor)
        pairs = longest = 0
        seen = [False] * n
        for start in range(n):
            if degree[start] == 0 or seen[start]:
                continue
            cycle = []
            node = start
            while not seen[node]:
                seen[node] = True
                cycle.append(node)
                node = favorite[node]
            if len(cycle) == 2:
                pairs += depth[cycle[0]] + depth[cycle[1]]
            else:
                longest = max(longest, len(cycle))
        return max(pairs, longest)
