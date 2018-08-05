from random import randint

class NPC_item(object):
    def __init__(self):
        self.Action_Total = randint(9,13)
        self.Close_Combat = randint(9,13)
        self.Defence = randint(4,5)
        self.Hit_Points = randint(20,30)

newItem = NPC_item()

for attr,value in newItem.__dict__.items():
    print(attr,": ",value)
