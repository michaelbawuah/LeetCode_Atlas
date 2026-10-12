def generate(rng):
    count = rng.randint(2, 9)
    rooms = [[key for key in range(count) if rng.random() < 0.3] for _ in range(count)]
    if not any(rooms):
        rooms[0] = [0]
    return [rooms]
