from kivy import Logger
from kivy.uix.screenmanager import ScreenManager, FadeTransition

from Classes.baseBuilderScreen import BaseBuilderScreen
from Classes.crashScreen import CrashScreen
from Classes.globals import get_Globals
from Classes.introScreen import IntroScreen

from Classes.baseBuilder import BaseBuilder
from Classes.betterFloatLayout import BetterFloatLayout



class ScreenManager(ScreenManager):
    def __init__(self):
        super(ScreenManager, self).__init__()

        Globals = get_Globals()

        self.width = Globals.width
        self.height = Globals.height

        introScreen = IntroScreen(name="IntroScreen")
        crashScreen = CrashScreen(name="CrashScreen")
        baseBuildScreen = BaseBuilderScreen(name="BaseBuilderScreen")

        self.add_widget(introScreen)
        self.add_widget(crashScreen)
        self.add_widget(baseBuildScreen)

        if Globals.User_data.get("introFinished"):
            self.current = "BaseBuilderScreen"
            Logger.info("Application: Starting in BaseBuilder")

        else:
            Logger.info("Application: Starting in Intro")
            self.current = "IntroScreen"

        Logger.info("Application: Screen Manager setup")

    def openCrashScreen(self, _=None):
        self.transition = FadeTransition()
        self.current = "CrashScreen"

    def openBaseBuilderScreen(self, _=None):
        self.transition = FadeTransition()
        self.current = "BaseBuilderScreen"
