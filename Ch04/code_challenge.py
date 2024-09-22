"""
Add fractions

You're given the numerator and denominator of two fractions. Use the fractions module to add the fractions together and return a tuple (numerator and denominator) with the sum.

Your task: Return the result of the two fractions added together.
"""

from fractions import Fraction

show_expected_result = False
show_hints = False

def add_fractions(numerator1, denominator1, numerator2, denominator2):
    # Use the Fraction class to add the two fractions
    result = Fraction(numerator1, denominator1) + Fraction(numerator2, denominator2)
    return (result.numerator, result.denominator)


if __name__ == "__main__":
    # Test your code with this first
    # Change the arguments to test different values
    print(add_fractions(6,5,1,5))