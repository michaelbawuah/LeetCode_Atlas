def generate(rng):
    airports = ["JFK", "AAA", "BBB", "CCC"]
    route = ["JFK"]
    for _ in range(rng.randint(1, 7)):
        route.append(rng.choice([airport for airport in airports if airport != route[-1]]))
    tickets = [[first, last] for first, last in zip(route, route[1:], strict=False)]
    rng.shuffle(tickets)
    return [tickets]
