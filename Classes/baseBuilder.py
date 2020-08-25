from kivy.graphics import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

from Classes.globals import get_Globals


class BaseBuilder(Widget):
    def __init__(self, *args, **kwargs):
        super(BaseBuilder, self).__init__(*args, **kwargs)

        self.Globals = get_Globals()

        self.size = self.Globals.width, self.Globals.width

        self.bg = FloatLayout()
        self.baseBuilder = FloatLayout()

        self.draw()

        self.add_widget(self.bg)
        self.add_widget(self.baseBuilder)


    def draw(self):
        self.bg.canvas.before.clear()
        self.baseBuilder.canvas.clear()

        with self.bg.canvas.before:
            Rectangle(pos=self.pos, size=self.size, texture=self.Globals.Textures.planetSurface)

        with self.baseBuilder.canvas.before:
            building_layout = self.Globals.User_data.get("building_layout")
            for buildingId in building_layout:
                print(buildingId, building_layout[buildingId])
