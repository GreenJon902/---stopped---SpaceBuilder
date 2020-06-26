from kivy.graphics import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

from Classes.globals import get_Globals


class BaseBuilder(Widget):
    def __init__(self, *args, **kwargs):
        super(BaseBuilder, self).__init__(*args, **kwargs)

        self.Globals = get_Globals()

        self.canyon = FloatLayout()
        self.baseBuilder = FloatLayout()
        self.defences = FloatLayout()

        self.draw()


    def draw(self):
        self.canyon.canvas.clear()
        self.baseBuilder.canvas.clear()
        self.defences.canvas.clear()

        with self.canyon.canvas:
            Rectangle(pos=self.pos, size=self.size, texture=self.Globals.Textures.canyon_background)
