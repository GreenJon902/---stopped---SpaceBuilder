from kivy import Logger
from kivy.uix.screenmanager import ScreenManager

from Classes.baseBuilderScreen import BaseBuilderScreen
from Classes.crashScreen import CrashScreen
from Classes.introScreen import IntroScreen


class ScreenManager(ScreenManager):
    def __init__(self, Globals):
        super(ScreenManager, self).__init__()

        introScreen = IntroScreen(Globals, name="IntroScreen")
        crashScreen = CrashScreen(Globals, name="IntroScreen")
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

    def openCrashScreen(self, _):
        self.current = "CrashScreen"
