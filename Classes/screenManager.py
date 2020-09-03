from kivy import Logger
from kivy.uix.screenmanager import ScreenManager, FadeTransition

from Classes.baseBuilderScreen import BaseBuilderScreen
from Classes.introCrashScreen import CrashScreen
from Classes.globals import get_Globals
from Classes.introShipScreen import IntroScreen
from Classes.buildingScreen import BuildingScreen
from Classes.settingsScreen import SettingsScreen
from Classes.screen import Screen

from Classes.baseBuilder import BaseBuilder
from Classes.betterFloatLayout import BetterFloatLayout
from Classes.betterScatter import BetterScatter
from Classes.sizedButton import SizedButton
from Classes.itemsWidget import ItemsWidget
from Classes.heightBasedButton import HeightBasedButton



class ScreenManager(ScreenManager):
    def __init__(self):
        super(ScreenManager, self).__init__()

        Globals = get_Globals()

        self.width = Globals.width
        self.height = Globals.height


        #  So things actually work
        dumpScreen = Screen(name="DumpScreen")
        self.add_widget(dumpScreen)

        #  Intro Screens
        introScreen = IntroScreen(name="IntroShipScreen")
        crashScreen = CrashScreen(name="IntroCrashScreen")
        self.add_widget(introScreen)
        self.add_widget(crashScreen)

        # Main Screens
        baseBuildScreen = BaseBuilderScreen(name="BaseBuilderScreen")
        self.add_widget(baseBuildScreen)

        #  Settings Screens
        settingsScreen = SettingsScreen(name="SettingsScreen")
        self.add_widget(settingsScreen)

        #  Inventory Screens
        buildingScreen = BuildingScreen(name="BuildingScreen")
        self.add_widget(buildingScreen)




        if Globals.User_data.get("introFinished"):
            self.current = "BaseBuilderScreen"
            Logger.info("Application: Starting in BaseBuilder")

        else:
            Logger.info("Application: Starting in Intro")
            self.current = "IntroShipScreen"

        Logger.info("Application: Screen Manager setup")


    def openBaseBuilderScreen(self, _=None):
        self.transition = FadeTransition()
        self.current = "BaseBuilderScreen"

    def sendTo(self, sendTo, _=None):
        self.transition = FadeTransition()
        self.current = sendTo
