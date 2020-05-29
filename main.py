import os

from kivy.app import App
from kivy.uix.label import Label
from kivy.logger import Logger
import Global


Globals = Global.Globals()


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
        return Label(text="Hello World")



if __name__ == '__main__':
    SpaceBuilder().run()
