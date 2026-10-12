def generate(rng):
    genes = [a + b + "AAAAAA" for a in "ACGT" for b in "ACGT"]
    start, end = rng.sample(genes, 2)
    return [start, end, rng.sample(genes, rng.randint(0, 10))]
