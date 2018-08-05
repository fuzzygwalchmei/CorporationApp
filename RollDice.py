from random import randint

def diceRoller(quantity, die, modifier):
  rolls = []
  for each in range(quantity):
    rolls.append(randint(1,die))
  return rolls


quantity = int(input("Enter the number of dice: "))
die = int(input("Enter the type of die: "))
modifier = int(input("Enter the modifier: "))

myRolls = diceRoller(quantity,die,modifier)
rollTotal = sum(myRolls) + modifier

if modifier >= 0:
    print("You rolled ",quantity,"d",die,"+",modifier)
else:
    print("You rolled ",quantity,"d",die,modifier)

print("Rolls: ",myRolls,"- Total: ", rollTotal)
