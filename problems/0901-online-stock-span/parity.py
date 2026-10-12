"""Generate valid inputs for reproducible cross-language comparisons."""


def generate(rng):
    prices = [
        rng.choice([1, 100000, 100, 200, rng.randint(1, 100000)])
        for _ in range(rng.randint(1, 100))
    ]
    return [["StockSpanner"] + ["next"] * len(prices), [[]] + [[price] for price in prices]]
