import re

diceString = input("Enter your dice string: ")

qty,die,mod = re.split('[d + -]',diceString)

if "-" in diceString:
    print("Qty: ",qty,", Die: ",die,", Mod: ",0-int(mod))
else:
    print("Qty: ",qty,", Die: ",die,", Mod: ",mod)
