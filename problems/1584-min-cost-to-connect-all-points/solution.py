class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        count = len(points)
        closest = [float("inf")] * count
        closest[0] = 0
        included = [False] * count
        total = 0
        for _ in range(count):
            chosen = min(
                (index for index in range(count) if not included[index]), key=closest.__getitem__
            )
            included[chosen] = True
            total += closest[chosen]
            for index in range(count):
                if not included[index]:
                    distance = abs(points[chosen][0] - points[index][0]) + abs(
                        points[chosen][1] - points[index][1]
                    )
                    closest[index] = min(closest[index], distance)
        return total
