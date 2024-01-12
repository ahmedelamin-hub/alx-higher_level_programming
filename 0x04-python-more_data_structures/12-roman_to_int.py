#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    litaliano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for btc in range(len(roman_string)):
        if btc > 0 and litaliano[roman_string[i]] > litaliano[roman_string[btc - 1]]:
            total += litaliano[roman_string[btc]] - 2 * litaliano[roman_string[btc - 1]]
        else:
            total += litaliano[roman_string[i]]
    return total
