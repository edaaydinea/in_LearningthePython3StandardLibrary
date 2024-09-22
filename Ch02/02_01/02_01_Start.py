# Math Module Part I

import math  # Import the math module

# Constants
print(math.pi)  # Print the value of pi
print(math.e)   # Print the value of Euler's number

print(math.nan)  # Print the value of NaN (Not a Number)
print(math.inf)  # Print the value of positive infinity
print(-math.inf) # Print the value of negative infinity

# Trigonometry
obst_direction = math.cos(math.pi / 4)  # Calculate the cosine of 45 degrees (pi/4 radians)
print(obst_direction)  # Print the cosine value
print(math.sin(math.pi / 4))  # Calculate and print the sine of 45 degrees (pi/4 radians)

# Ceiling and Floor
cookies = 10.3
candy = 7
print(math.ceil(cookies))  # Print the ceiling value of cookies (smallest integer >= cookies)
print(math.ceil(candy))    # Print the ceiling value of candy (smallest integer >= candy)

age = 47.9
otherAge = 47
print(math.floor(age))  # Print the floor value of age (largest integer <= age)
print(math.floor(otherAge))  # Print the floor value of otherAge (largest integer <= otherAge)