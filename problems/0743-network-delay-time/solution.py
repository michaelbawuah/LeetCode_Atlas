from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adjacency = [[] for _ in range(n + 1)]
        for first, second, delay in times:
            adjacency[first].append((second, delay))
        distances = [float("inf")] * (n + 1)
        distances[k] = 0
        pending = [(0, k)]
        while pending:
            elapsed, node = heappop(pending)
            if elapsed != distances[node]:
                continue
            for neighbor, delay in adjacency[node]:
                arrival = elapsed + delay
                if arrival < distances[neighbor]:
                    distances[neighbor] = arrival
                    heappush(pending, (arrival, neighbor))
        answer = max(distances[1:])
        return -1 if answer == float("inf") else answer
