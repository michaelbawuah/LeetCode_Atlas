def generate(rng):
    size = rng.randint(1, 80)
    # Both the bounded state-DP branch and the unlimited-transactions branch.
    budget = rng.choice([1, rng.randint(1, min(100, size)), 100])
    return [budget, [rng.randint(0, 1000) for _ in range(size)]]
