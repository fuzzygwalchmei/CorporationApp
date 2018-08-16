from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from random import randint
from NPC_generator import *
from kivy.properties import NumericProperty, StringProperty, BooleanProperty,\
    ListProperty

class CorporationScreen(Screen):

    pass

class CorporationApp(App):
    NPC_List = ListProperty([])
    def Add_NPC(self):
        listLength = len(self.NPC_List)
        newNPC = NPC_item(listLength)
        self.NPC_List.append(newNPC)

        #for attr,value in newNPC.__dict__.items():
        #    print(attr,": ",value)

        for each in self.NPC_List:
            for attr,value in each.__dict__.items():
                print(attr,": ",value, )

    def build(self):
        return CorporationScreen()


if __name__ == '__main__':
    CorporationApp().run()
