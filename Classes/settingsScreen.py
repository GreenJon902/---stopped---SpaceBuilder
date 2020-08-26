from kivy import Logger

from Classes.screen import Screen


class SettingsScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(SettingsScreen, self).__init__(*args, **kwargs)

    def post_enter(self):
        Logger.info("Application: Settings Screen entered")

    def post_init(self):
        Logger.info("Application: Settings Screen widgets setup")
