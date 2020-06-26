from kivy.graphics import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class BaseBuilder(Widget):
    def __init__(self, *args, **kwargs):
        super(self, BaseBuilder).__init__(*args, **kwargs)

        self.Globals = None

        self.canyon = FloatLayout()
        self.baseBuilder = FloatLayout()
        self.defences = FloatLayout()


    def draw(self):
        self.canyon.canvas.clear()
        self.baseBuilder.canvas.clear()
        self.defences.canvas.clear()

        with self.canyon.canvas:
            Rectangle(pos=self.pos, size=self.size, texture=self.Globals.Textures.canyon_background)
