import os
import sys

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.logger import Logger

from Classes.globals import Globals
from Classes.screenManager import ScreenManager

Builder.load_file('kv.kv')


class SpaceBuilder(App):
    def __init__(self):
        super(SpaceBuilder, self).__init__()
        Window.size = 1000, 500

        self.setup()

        Globals.width = Window.width
        Globals.height = Window.height

    def setup(self):
        Logger.info("Application: Starting setup")

        Globals.User_data.save_path = str(os.path.join(str(self.user_data_dir), "user_data.json"))
        Globals.Settings_data.save_path = str(os.path.join(str(self.user_data_dir), "settings_data.json"))

        Logger.info("Application: Finished setup")

    def build(self):
        return ScreenManager(Globals)

    def on_stop(self):
        sys.exit()


if __name__ == '__main__':
    Globals = Globals()
    SpaceBuilder().run()
