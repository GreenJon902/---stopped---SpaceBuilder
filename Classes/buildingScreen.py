from kivy import Logger

from Classes.screen import Screen


class BuildingScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(BuildingScreen, self).__init__(*args, **kwargs)

    def post_enter(self):
        Logger.info("Application: Building Screen entered")

    def post_init(self):
        Logger.info("Application: Building Screen widgets setup")