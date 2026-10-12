"""Generate valid inputs for reproducible cross-language comparisons."""


def generate(rng):
    number = rng.randint(1, 2**31 - 1)
    title = ""
    while number:
        number, digit = divmod(number - 1, 26)
        title = chr(65 + digit) + title
    return [title]
