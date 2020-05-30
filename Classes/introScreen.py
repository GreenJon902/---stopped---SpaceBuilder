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
        self.clock = Clock.schedule_interval(lambda x: self.draw(self.Globals), 0.5)

    def draw(self, Globals):
        with self.canvas:
            self.canvas.clear()

            Color(1, 1, 1)

            x, y = random.randint(0, Globals.width), random.randint(0, Globals.height)

            Rectangle(pos=(x, y), size=(Globals.width / 10, Globals.height / 50))

    def on_leave(self, *args):
        self.clock.cancel()
