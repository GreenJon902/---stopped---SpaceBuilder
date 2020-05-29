import os

from kivy.app import App
from kivy.lang import Builder
from kivy.logger import Logger

from Classes.globals import Globals
from Classes.screenController import ScreenController

Builder.load_file('kv.kv')


class SpaceBuilder(App):
    def __init__(self):
        super(SpaceBuilder, self).__init__()

        self.setup()

    def setup(self):
        Logger.info("Application: Starting setup")

        Globals.User_data.save_path = str(os.path.join(str(self.user_data_dir), "user_data.json"))
        Globals.Settings_data.save_path = str(os.path.join(str(self.user_data_dir), "settings_data.json"))

        Logger.info("Application: Finished setup")

    def build(self):
        return ScreenController(Globals)


if __name__ == '__main__':
    Globals = Globals()
    SpaceBuilder().run()
