# Importing the statistics and math modules
import statistics
import math

# Sample data: ages of a group of people
agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]

# Calculate and print the mean (average) of the ages
print(statistics.mean(agesData))

# Calculate and print the mode (most common value) of the ages
print(statistics.mode(agesData))

# Calculate and print the median (middle value) of the ages
print(statistics.median(agesData))

# Print the sorted list of ages
print(sorted(agesData))

# Calculate and print the variance of the ages
print(statistics.variance(agesData))

# Calculate and print the standard deviation of the ages
print(statistics.stdev(agesData))

# Calculate and print the square root of the variance (should be equal to the standard deviation)
print(math.sqrt(statistics.variance(agesData)))
