def generate(rng):
    prices = [rng.randint(1, 49999) for _ in range(rng.randint(1, 60))]
    mode = rng.randrange(4)
    if mode == 0:
        prices.sort()
    elif mode == 1:
        prices.sort(reverse=True)
    return [prices, 0 if mode == 2 else rng.randint(0, 49999)]
