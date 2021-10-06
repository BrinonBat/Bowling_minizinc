from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

from menu import *
from score import *
from complete import *


class WindowManager(ScreenManager):
    def generate(self, score):
        generate(self, score)

    def complete(self, score, partie):
        complete(self, score, partie)


Config.set('graphics', 'width', '1414')
Config.set('graphics', 'height', '1080')

kv = Builder.load_file("main.kv")


class MainApp(App):
    def build(self):
        return kv


MainApp().run()
