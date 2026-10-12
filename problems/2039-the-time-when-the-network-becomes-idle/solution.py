from collections import deque


class Solution:
    def networkBecomesIdle(self, edges: list[list[int]], patience: list[int]) -> int:
        adjacent = [[] for _ in patience]
        for a, b in edges:
            adjacent[a].append(b)
            adjacent[b].append(a)
        distance = [-1] * len(patience)
        distance[0] = 0
        pending = deque([0])
        while pending:
            node = pending.popleft()
            for neighbor in adjacent[node]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[node] + 1
                    pending.append(neighbor)
        last = 0
        for node in range(1, len(patience)):
            round_trip = 2 * distance[node]
            resend = ((round_trip - 1) // patience[node]) * patience[node]
            last = max(last, resend + round_trip)
        return last + 1
