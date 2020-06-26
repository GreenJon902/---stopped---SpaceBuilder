import sys

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window

from Classes.baseScreenManager import BaseScreenManager
from Classes.globals import get_Globals
from Classes.loadingScreen import LoadingScreen
from Classes.screenManager import ScreenManager
from loadFunctions import create_Globals, load_kv, load_textures, add_save_paths, load_audio


class SpaceBuilder(App):
    def __init__(self):
        super(SpaceBuilder, self).__init__()
        Window.size = 1000, 500

        self.baseScreenManager = None


    def build(self):

        loadingScreen = LoadingScreen()
        loadingScreen.app = self


        loadingScreen.bus.append(("Loading KV", load_kv))
        loadingScreen.bus.append(("Create Globals", create_Globals))
        loadingScreen.bus.append(("Adding save paths", add_save_paths))
        loadingScreen.bus.append(("Loading Textures", load_textures))
        loadingScreen.bus.append(("Loading Audio", load_audio))


        Clock.schedule_once(loadingScreen.start_bus, 0)

        self.baseScreenManager = BaseScreenManager(loadingScreen, ScreenManager)

        return self.baseScreenManager

    def on_stop(self):
        Globals = get_Globals()
        Globals.User_data.save()
        Globals.Settings_data.save()

        sys.exit()
