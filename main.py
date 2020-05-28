import os

from kivy.app import App
from kivy.uix.label import Label
from kivy.logger import Logger
from Global import Global


class SpaceBuilder(App):
    def __init__(self):
        super(SpaceBuilder, self).__init__()

        self.setup()

    def setup(self):
        Logger.info("Application: Starting setup")


        Global.save_path = os.path.join(self.user_data_dir, "user_data.json")
        Logger.info("Application: App data save path: " + Global.save_path)

        Global.User_data.load()
        Logger.info("Application: Loaded user data")


        Logger.info("Application: Finished setup")

    def build(self):
        return Label(text="Hello World")



if __name__ == '__main__':
    SpaceBuilder().run()
