# Python Rounding, Absolute Value, and Exponents

# round()
# Input: one whole number or one decimal number
# Output: integer that represents the inputted number, rounded up or down depending on its value
# First decimal digit 4 or below -> round down
# First decimal digit 5 or above -> round up

myGPA = 3.6
print(round(myGPA)) # 4

amountOfSalt = 1.4
print(round(amountOfSalt)) # 1


apple = -1.2
print(round(apple)) # -1

google = -1.6
print(round(google)) # -2

# abs()
# Abs: stands for absolute value
# Input: one whole or decimal number
# Output: number representing the absolute value of the inputted number
# Positive number -> same number returned
# Negative number -> positive version of input returned

distanceAway = -13
print(abs(distanceAway)) # 13

lengthOfRootInGround = -2.5
print(abs(lengthOfRootInGround)) # 2

# pow()

# Input: two whole or deciaml numbers
    # First input: base
    # Second input: exponent
# Output: number representing the result of the exponentiation

chanceOfTails = 0.5
inARowTails = 3
print(pow(chanceOfTails, inARowTails)) # 0.125

chanceOfOne = .167
inARowOne = 2
print(pow(chanceOfOne, inARowOne)) # 0.027889