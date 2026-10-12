from collections import defaultdict
from heapq import heapify, heappop


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adjacent = defaultdict(list)
        for start, end in tickets:
            adjacent[start].append(end)
        for destinations in adjacent.values():
            heapify(destinations)
        pending, reversed_route = ["JFK"], []
        while pending:
            if adjacent[pending[-1]]:
                pending.append(heappop(adjacent[pending[-1]]))
            else:
                reversed_route.append(pending.pop())
        return reversed_route[::-1]
