from kivy import Logger
from kivy.animation import Animation
from kivy.core.image import Image as CoreImage
from kivy.clock import Clock
from kivy.graphics import *

from Classes.screen import Screen


class CrashScreen(Screen):
    def __init__(self, Globals, *args, **kwargs):
        super(CrashScreen, self).__init__(*args, **kwargs)

        self.Globals = Globals

        self.canyonClock = None
        self.starClock = None


        ratio = CoreImage("textures/canyon surface.png").width / CoreImage("textures/canyon surface.png").height
        self.h = self.Globals.height
        self.w = ratio * Globals.width

        self.starLayout = self.ids["stars"]
        self.canyonLayout = self.ids["canyon"]

        self.starLayout.pos = (Globals.width, 0)
        self.canyonLayout.pos = (Globals.width, 0)

        with self.starLayout.canvas:
            Rectangle(pos=self.starLayout.pos, size=(self.w, self.h), source="textures/canyon surface stars.png")

        with self.canyonLayout.canvas:
            Rectangle(pos=self.starLayout.pos, size=(self.w, self.h), source="textures/canyon surface.png")

        Logger.info("Application: Crash Screen setup")


    def post_init(self):
        Logger.info("Application: Crash Screen entered")

        self.canyonClock = Clock.schedule_interval(self.move_canyon, self.Globals.GameSettings.intro_move_delay)
        self.starClock = Clock.schedule_interval(self.move_stars, self.Globals.GameSettings.intro_move_delay)


    def move_canyon(self, _):
        animation = Animation(pos=self.starLayout.pos, duration=0)
        animation += Animation(pos=(self.starLayout.pos[0] + self.starLayout.width, self.starLayout.pos[1]),
                               duration=self.Globals.GameSettings.crash_move_length)

        animation.start(self.canyonLayout)


    def move_stars(self, _):
        pass
