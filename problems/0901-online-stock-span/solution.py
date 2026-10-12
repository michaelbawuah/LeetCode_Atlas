class StockSpanner:
    def __init__(self):
        self._pending = []

    def next(self, price: int) -> int:
        span = 1
        while self._pending and self._pending[-1][0] <= price:
            span += self._pending.pop()[1]
        self._pending.append((price, span))
        return span
