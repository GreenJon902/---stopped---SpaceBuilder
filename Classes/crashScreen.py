from kivy import Logger
from kivy.clock import Clock

from Classes.screen import Screen


class CrashScreen(Screen):
    def __init__(self, Globals, *args, **kwargs):
        super(CrashScreen, self).__init__(*args, **kwargs)

        self.Globals = Globals

        self.canyonClock = None
        self.starClock = None

        self.starsLayout = self.ids["stars"]
        self.canyonLayout = self.ids["canyon"]

        Logger.info("Application: Crash Screen setup")

    def post_init(self):
        Logger.info("Application: Crash Screen entered")

        self.canyonClock = Clock.schedule_interval(self.move_canyon, self.Globals.GameSettings.intro_move_delay)
        self.starClock = Clock.schedule_interval(self.move_stars, self.Globals.GameSettings.intro_move_star)

    def move_canyon(self, _):
        pass

    def move_stars(self, _):
        pass
