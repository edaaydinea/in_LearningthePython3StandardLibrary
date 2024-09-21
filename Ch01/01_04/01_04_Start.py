# Range -> range instance that holds all nums counting by one between 0 and first input
# List -> lists numbers from the inputted tuple

numberedContestants = range(30) # range instance that holds all nums counting by one between 0 and first input

print(list(numberedContestants)) # lists numbers from the inputted tuple

for c in list(numberedContestants):
    print("Contestant " + str(c) + " is here")
    
luckyWinners = range(7, 30, 5) # range instance that holds all nums counting by five between 7 and 30

print(list(luckyWinners)) # lists numbers from the inputted tuple