def generate(rng):
    m, n = rng.randint(0, 20), rng.randint(0, 20)
    if m + n == 0:
        n = 1
    first = sorted(rng.randint(-20, 20) for _ in range(m))
    second = sorted(rng.randint(-20, 20) for _ in range(n))
    return [first + [0] * n, m, second, n]
