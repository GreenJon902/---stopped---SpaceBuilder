from kivy import Logger

from Classes.screen import Screen


class CrashScreen(Screen):
    def __init__(self, Globals, *args, **kwargs):
        super(CrashScreen, self).__init__(*args, **kwargs)

        self.Globals = Globals

        self.starsLayout = self.ids["stars"]
        self.canyonLayout = self.ids["canyon"]

        Logger.info("Application: Crash Screen setup")

    def post_init(self):
        Logger.info("Application: Crash Screen entered")
