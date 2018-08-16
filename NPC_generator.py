from random import randint

class NPC_item(object):

    def __init__(self,myVal=0):
        self.myRef = "NPC#: "+str(myVal)
        self.Action_Total = randint(9,13)
        self.Close_Combat = randint(9,13)
        self.Defence = randint(4,5)
        self.Hit_Points = randint(20,30)

    def Number_Generator(self):
        for each in range(1,1000):
            yield each

newItem = NPC_item()

for attr,value in newItem.__dict__.items():
    print(attr,": ",value)
