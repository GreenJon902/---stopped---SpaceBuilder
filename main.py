import sys

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window

from Classes.loadingScreen import LoadingScreen
from Classes.screenManager import ScreenManager
from loadFunctions import create_Globals, add_save_paths, load_kv, load_textures


class SpaceBuilder(App):
    def __init__(self):
        super(SpaceBuilder, self).__init__()
        Window.size = 1000, 500

        self.Globals = None


    def build(self):

        loadingScreen = LoadingScreen()
        loadingScreen.app = self
        loadingScreen.nextWidget = ScreenManager


        loadingScreen.bus.append(("Loading KV", load_kv))
        loadingScreen.bus.append(("Create Globals", create_Globals))
        loadingScreen.bus.append(("Adding save paths", add_save_paths))
        loadingScreen.bus.append(("Loading Textures", load_textures))




        Clock.schedule_once(loadingScreen.start_bus, 0)

        return loadingScreen

    def on_stop(self):
        sys.exit()


if __name__ == '__main__':
    SpaceBuilder().run()
