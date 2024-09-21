"""
Count valid numbers in a list

You're given a list of integers. Valid numbers are those with absolute values that fall within the upper and lower range (inclusive) provided as input.

Task: Return the number of valid numbers in the list.
"""

show_expected_result = False
show_hints = False 

def count_valid(numbers, lower, upper):
    valid_numbers = 0
    for number in numbers:
        if abs(number) >= lower and abs(number) <= upper:
            valid_numbers += 1
    return valid_numbers
