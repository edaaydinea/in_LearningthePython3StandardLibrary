# Import the random module to generate random numbers and make random choices
import random

# Generate a random float number between 0.0 and 1.0
print(random.random())

# Generate a random integer between 0 and 1
decider = random.randrange(2)

# Use the random integer to decide between "HEADS" and "TAILS"
if decider == 0:
    print("HEADS")
else:
    print("TAILS")

# Print the random integer used for the decision
print(decider)

# Generate a random integer between 1 and 6 (inclusive) to simulate rolling a die
print("You rolled a " + str(random.randrange(1, 7)))

# Generate a list of 5 unique random numbers between 0 and 99 to simulate lottery winners
lotteryWinners = random.sample(range(100), 5)
print(lotteryWinners)

# Choose a random pet from the list of possible pets
possiblePets = ["cat", "dog", "fish"]
print(random.choice(possiblePets))

# Shuffle a list of cards and print the shuffled list
cards = ["Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
print(cards)