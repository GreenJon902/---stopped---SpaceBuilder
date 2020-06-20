import sys

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window

import loadFunctions
from Classes.BaseScreenManager import BaseScreenManager
from Classes.loadingScreen import LoadingScreen
from Classes.screenManager import ScreenManager


class SpaceBuilder(App):
    def __init__(self):
        super(SpaceBuilder, self).__init__()
        Window.size = 1000, 500

        self.Globals = None
        self.baseScreenManager = None


    def build(self):

        loadingScreen = LoadingScreen()
        loadingScreen.app = self

        loadFunctions.bus = loadFunctions.append(loadingScreen.bus)

        Clock.schedule_once(loadingScreen.start_bus, 0)

        self.baseScreenManager = BaseScreenManager(loadingScreen, lambda: ScreenManager(self.Globals))

        return self.baseScreenManager

    def on_stop(self):
        sys.exit()


if __name__ == '__main__':
    SpaceBuilder().run()
