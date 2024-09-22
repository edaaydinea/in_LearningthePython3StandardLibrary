# Itertools Part 2
import itertools

# Permutations: Order matters - generates all possible orderings of the input
election = {1: "Barb", 2:"Karen", 3:"Erin"}
# Permutations of the keys of the election dictionary
for p in itertools.permutations(election):
    print(p)

# Permutations of the values of the election dictionary
for p1 in itertools.permutations(election.values()):
    print(p1)

# Combinations: Order does not matter - generates all possible combinations of the input
colorsForPainting = ["Red", "Blue", "Purple", "Orange", "Yellow", "Pink"]
# Combinations of 3 colors from the colorsForPainting list
for c in itertools.combinations(colorsForPainting, 3):
    print(c)