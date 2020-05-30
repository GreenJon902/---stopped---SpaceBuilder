from kivy.uix.screenmanager import ScreenManager

from Classes.baseBuilderScreen import BaseBuilderScreen
from Classes.introScreen import IntroScreen


class ScreenController(ScreenManager):
    def __init__(self, Globals):
        super(ScreenController, self).__init__()




        introScreen = IntroScreen(Globals, name="IntroScreen")
        baseBuildScreen = BaseBuilderScreen(name="BaseBuildScreen")


        self.add_widget(introScreen)
        self.add_widget(baseBuildScreen)


        if Globals.User_data.get("introFinished"):
            self.current = "BaseBuildScreen"

        else:
            self.current = "IntroScreen"
