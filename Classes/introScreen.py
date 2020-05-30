import random
import threading

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.graphics import *


class IntroScreen(Screen):
    def __init__(self, Globals, *args, **kwargs):
        super(IntroScreen, self).__init__(*args, **kwargs)
        self.clock = None
        self.Globals = Globals

    def on_enter(self, *args):
        self.clock = Clock.schedule_interval(self.draw, 0.1)

    def draw(self, _):
        self.canvas.clear()

        Globals = self.Globals

        for i in range(Globals.GameSettings.intro_star_amount):
            with self.canvas:
                Color(1, 1, 1)

                x, y = Globals.width / 10 * -1, Globals.height / 10 * -1
                x2, y2 = random.randint(0, Globals.width), random.randint(0, Globals.height / 2) + Globals.height / 2

                width, height = Globals.width + (x * 2), Globals.height + (y * 2)

                Rectangle(pos=(x2, y2), size=(Globals.width / Globals.GameSettings.intro_star_width_divider,
                                              Globals.height / Globals.GameSettings.intro_star_height_divider),
                          color=Color(1, 1, 1))
                Rectangle(pos=(x, y), size=(width, height), source="textures/shipInside.png")
                # Rectangle(pos=(x - 10, y - 10), size=(Globals.width / 10 + 10, Globals.height / 50 + 10),
                #         color=Color(1, 0, 0, 0.1))

    def on_leave(self, *args):
        self.clock.cancel()
