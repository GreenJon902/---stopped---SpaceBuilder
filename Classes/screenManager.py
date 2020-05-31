from kivy import Logger
from kivy.uix.screenmanager import ScreenManager

from Classes.baseBuilderScreen import BaseBuilderScreen
from Classes.introScreenType1 import IntroScreenType1
from Classes.rotatableFloatLayout import RotatableFloatLayout


class ScreenManager(ScreenManager):
    def __init__(self, Globals):
        super(ScreenManager, self).__init__()


        if Globals.GameSettings.intro_type == 1:
            introScreen = IntroScreenType1(Globals, name="IntroScreen")

        elif Globals.GameSettings.intro_type == 2:
            pass

        else: Logger.warn("Application: There is not intro type " + Globals.GameSettings.intro_type)


        baseBuildScreen = BaseBuilderScreen(name="BaseBuilderScreen")


        self.add_widget(introScreen)
        self.add_widget(baseBuildScreen)


        if Globals.User_data.get("introFinished"):
            self.current = "BaseBuilderScreen"
            Logger.info("Application: Starting in BaseBuilder")

        else:
            Logger.info("Application: Starting in Intro")
            self.current = "IntroScreen"

        Logger.info("Application: Screen Manager setup")
