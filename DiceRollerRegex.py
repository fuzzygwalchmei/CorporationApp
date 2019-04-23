import re
import random

diceRegex = "[\d][d|D][\d]"
modRegex = "[\-|\+]*\s[\d][^d|D]"

def getItems(diceInput):
    myDice = re.findall(diceRegex,diceInput)
    myMods = re.findall(modRegex,diceInput)
    rolls= []
    mods=[]

    for each in myDice:
        numDice,typeDice = re.split('[d D]',each)
        rolls.append(diceRoll(int(numDice),int(typeDice)))


    for each in myMods:
        each=each.replace(" ","")
        mods.append(int(each))

    print("Rolls: ",rolls) #, sum(rolls)
    print("Mods: ",mods) #, sum(mods)
    sumRolls = sum(list(map(sum, rolls)))
    sumMods = sum(mods)
    print(sumRolls + sumMods)


def diceRoll(numDice,typeDice):
    rolls = []
    for each in range(numDice):
        rolls.append(random.randint(1,typeDice))
    return rolls


diceInput = input("What dice do you want to roll?: ")
getItems(diceInput)
