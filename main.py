# camrat/main.py
from kivy.app import App
from kivy.uix.label import Label

class CamRat(App):
    def build(self):
        return Label(text="Battery Optimization Service Running")

CamRat().run()