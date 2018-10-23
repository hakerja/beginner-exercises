# program to roll dice for you
# ask user how many dice, and how many sides on each die
import random

def rollDice():
    numDice = int(input("How many dice would you like to roll?\n"))
    numSides = int(input("How many sides are on each die?\n"))
    print("You are rolling " + str(numDice) + " and each die has " + str(numSides) + " sides.")
    isReady = input("Ready to roll? (Y/N)\n")
    if isReady.upper().strip() == "N":
        print("Goodbye")
    elif isReady.upper().strip() == "Y":
        diceList = []
        total = 0
        for x in range(numDice):
            a = random.randint(1,numSides)
            diceList.append(a)
            total += a
        print("You rolled: " + str(diceList))
        print("Total: " + str(total))

if __name__ == '__main__':
    rollDice()
