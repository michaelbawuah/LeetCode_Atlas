def generate(rng):
    n = rng.randint(1, 7)
    recipes = ["r" + chr(97 + i) for i in range(n)]
    supplies = ["water", "salt", "flour"][: rng.randint(1, 3)]
    universe = recipes + ["water", "salt", "flour", "unknown"]
    ingredients = [rng.sample(universe, rng.randint(1, min(4, len(universe)))) for _ in recipes]
    return [recipes, ingredients, supplies]
