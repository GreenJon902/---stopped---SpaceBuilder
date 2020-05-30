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

        self.shakeScreenX = Globals.width / Globals.GameSettings.intro_ship_shake_amount_divider * -1
        self.shakeScreenY = Globals.height / Globals.GameSettings.intro_ship_shake_amount_divider * -1
        self.shakeScreenMoveDirections = random.choices(["up", "down", "left", "right", "upLeft", "upRight", "downLeft",
                                                         "downRight"],
                                                        k=self.Globals.GameSettings.intro_ship_shake_repeats)
        self.shakeScreenWidth = Globals.width - (self.shakeScreenX * 2)
        self.shakeScreenHeight = Globals.height - (self.shakeScreenY * 2)
        self.shakeScreenLayout = self.ids["shakeScreen"]

        self.shake()

    def on_enter(self, *args):
        self.clock = Clock.schedule_interval(self.draw, 0.1)

    def draw(self, _):
        self.shakeScreenLayout.canvas.clear()

        Globals = self.Globals

        for i in range(Globals.GameSettings.intro_star_amount):
            with self.shakeScreenLayout.canvas:
                Color(1, 1, 1)

                x, y = random.randint(0, Globals.width), random.randint(0, Globals.height / 2) + Globals.height / 2

                Rectangle(pos=(x, y), size=(Globals.width / Globals.GameSettings.intro_star_width_divider,
                                            Globals.height / Globals.GameSettings.intro_star_height_divider))
                Rectangle(pos=(self.shakeScreenX, self.shakeScreenY), size=(self.shakeScreenWidth,
                                                                            self.shakeScreenHeight),
                          source="textures/shipInside.png")
                # Rectangle(pos=(x - 10, y - 10), size=(Globals.width / 10 + 10, Globals.height / 50 + 10),
                #         color=Color(1, 0, 0, 0.1))

    def shake(self):
        for n, direction in enumerate(self.shakeScreenMoveDirections):
            print(n, direction)

    def on_leave(self, *args):
        self.clock.cancel()
