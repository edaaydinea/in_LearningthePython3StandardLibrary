# Create a range object from 0 to 29
r = range(0, 30)

# Print the type of the range object
print(type(r))

# Print the type of an integer
print(type(10))

# Print the type of a single character string
print(type('a'))

# Print the type of a string
print(type("Hi there"))

# Define an empty class Car
class Car:
    pass

# Define an empty class Truck
class Truck:
    pass

# Create instances of Car and Truck
c = Car()
convert = Car()
t = Truck()

# Print the type of the Car instance
print(type(c))

# Print the type of the Truck instance
print(type(t))

# Check if the types of c and t are the same
print(type(c) == type(t))

# Check if the types of c and convert are the same
print(type(c) == type(convert))

# Check if c is an instance of Car
print(isinstance(c, Car))

# Check if t is an instance of Car
print(isinstance(t, Car))

# If r is an instance of range, convert it to a list and print it
if isinstance(r, range):
    print(list(r))