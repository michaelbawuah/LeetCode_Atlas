class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        costs = [float("inf")] * n
        costs[src] = 0
        for _ in range(k + 1):
            next_costs = costs.copy()
            for first, second, price in flights:
                next_costs[second] = min(next_costs[second], costs[first] + price)
            costs = next_costs
        return -1 if costs[dst] == float("inf") else costs[dst]
