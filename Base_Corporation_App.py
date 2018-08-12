from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import Screen

class CorporationScreen(Screen):
    pass



class CorporationApp(App):
    def build(self):
        return CorporationScreen()

if __name__ == '__main__':
    CorporationApp().run()
