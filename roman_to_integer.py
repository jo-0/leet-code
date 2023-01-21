# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/


from typing import Dict, List


SYMBOLS: Dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_int(s: str) -> int:
    number_list = get_numbers(s)
    return add(number_list)


def add(number_list: List[int]) -> int:
    """Add numbers to get the final sum"""
    sum: int = 0
    for n in number_list:
        sum += n

    return sum


def get_numbers(symbol: str) -> List[int]:
    """Convert string to a list of numbers"""
    roman: List[int] = []
    idx: int = 0
    for c in symbol:
        num_equivalent = SYMBOLS[c]
        # Add the first element
        if not roman:
            roman.append(num_equivalent)
            idx += 1
            continue

        # Check if previous value is greater than or equal to current value
        if roman[idx - 1] >= num_equivalent:
            roman.append(num_equivalent)
            idx += 1
        else:
            roman[idx - 1] = num_equivalent - roman[idx - 1]

    return roman


print("Number = ", roman_to_int("MCMXCIV"))
