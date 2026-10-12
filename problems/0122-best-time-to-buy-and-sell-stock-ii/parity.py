def generate(rng):
    prices = [rng.randint(0, 10000) for _ in range(rng.randint(1, 60))]
    mode = rng.randrange(4)
    if mode == 0:
        prices.sort()
    elif mode == 1:
        prices.sort(reverse=True)
    elif mode == 2:
        prices = [prices[0]] * len(prices)
    return [prices]
