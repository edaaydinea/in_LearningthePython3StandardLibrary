# Python code​​​​​​‌​‌‌‌‌​​‌​‌‌‌​‌‌‌‌‌​‌​​​​ below
# Use print("messages...") to debug your solution.

"""
Calculate the hypotenuse

You're given the length of two sides of a right-angled triangle. Consider the Pythagorean theorem to calculate the length of the hypotenuse. c = √(a^2 + b^2)

Create a function that takes two arguments, side_length_one and side_length_two, and returns the length of the hypotenuse.
"""

show_expected_result = False
show_hints = False

def calculate_hypotenuse(side_length_one, side_length_two):
    return (side_length_one ** 2 + side_length_two ** 2) ** 0.5