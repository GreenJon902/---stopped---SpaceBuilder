from kivy.clock import Clock
from kivy.graphics import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

from Classes.globals import get_Globals


class BaseBuilder(Widget):
    def __init__(self, *args, **kwargs):
        super(BaseBuilder, self).__init__(*args, **kwargs)
        self.drawClock = None

        self.Globals = get_Globals()

        self.size = self.Globals.width, self.Globals.width

        self.bg = FloatLayout()
        self.buildings = FloatLayout()

        self.create()

        self.add_widget(self.bg)
        self.add_widget(self.buildings)

    def post_enter(self):
        self.drawClock = Clock.schedule_interval(self.draw, self.Globals.GameSettings.base_builder_new_frame_delay)


    def draw(self, _=None):
        self.bg.canvas.before.clear()

        with self.bg.canvas.before:
            Rectangle(pos=self.pos, size=self.size, texture=self.Globals.Textures.planetSurface)

        for building in self.buildings.children:
            building.draw()

    def create(self):
        pass
