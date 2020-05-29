from kivy.uix.screenmanager import ScreenManager

from Classes.baseBuildScreen import BaseBuildScreen
from Classes.introScreen import IntroScreen


class ScreenController(ScreenManager):
    def __init__(self):
        super(self, ScreenController).__init__()


        introScreen = IntroScreen(name="IntroScreen")
        baseBuildScreen = BaseBuildScreen(name="BaseBuildScreen")

        self.add_widget(introScreen)
        self.add_widget(baseBuildScreen)
