"""Generate valid inputs for reproducible cross-language comparisons."""


def roman(n):
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return thousands[n // 1000] + hundreds[n // 100 % 10] + tens[n // 10 % 10] + ones[n % 10]


def generate(rng):
    return [roman(rng.randint(1, 3999))]
