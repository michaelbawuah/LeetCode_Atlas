from heapq import heappop, heappush


class MedianFinder:
    def __init__(self):
        self._lower = []
        self._upper = []

    def addNum(self, num: int) -> None:
        heappush(self._lower, -num)
        heappush(self._upper, -heappop(self._lower))
        if len(self._upper) > len(self._lower):
            heappush(self._lower, -heappop(self._upper))

    def findMedian(self) -> float:
        if len(self._lower) > len(self._upper):
            return float(-self._lower[0])
        return (-self._lower[0] + self._upper[0]) / 2.0
