# Import the itertools module
import itertools

# Infinite Counting
# This loop will start counting from 50 and increment by 5 each time
for x in itertools.count(50, 5):
    print(x)
    # Break the loop when x reaches 80
    if x == 80:
        break

x = 0
# Infinite Cycling
# This loop will cycle through the list [1, 2, 3, 4] indefinitely
for c in itertools.cycle([1, 2, 3, 4]):
    print(c)
    x = x + 1
    # Break the loop after 50 iterations
    if x > 50:
        break

# Infinite Repeating
# This loop will repeat the value True indefinitely
for r in itertools.repeat(True):
    print(r)
    x = x + 1
    # Break the loop after 100 iterations
    if x > 100:
        break