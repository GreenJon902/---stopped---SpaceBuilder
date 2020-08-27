from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, StringProperty, DictProperty, BooleanProperty
from kivy.graphics import *

from Classes.globals import get_Globals


class Building(Widget, ButtonBehavior):
    rotation = NumericProperty(0)
    frame = NumericProperty(0)
    frameStep = NumericProperty(1)
    lastFrame = NumericProperty(0)
    name = StringProperty("BuildingBase")
    data = DictProperty({})
    animated = BooleanProperty(False)
    rotatable = BooleanProperty(False)

    def __init__(self, *args, **kwargs):
        super(Building, self).__init__(*args, **kwargs)
        self.Globals = get_Globals()

        size = self.Globals.width / self.Globals.GameSettings.base_builder_building_size_divider
        self.size = size, size

        state = str(0)
        textureInfo = self.Globals.BuildingTextures.get_texture_info(self.name)
        for s in textureInfo:
            if textureInfo[s]["data"] == self.data:
                state = str(s)
                break

        self.frameStep = textureInfo[state]["frameStep"]
        self.lastFrame = textureInfo[state]["lastFrame"]
        self.animated = textureInfo[state]["animated"]
        self.rotatable = textureInfo[state]["rotatable"]

    def draw(self):
        self.canvas.clear()
        with self.canvas:
            Rectangle(pos=self.pos, size=self.size,
                      texture=self.Globals.BuildingTextures.get_texture(self.name, self.data, self.frame,
                                                                        self.rotation))

        if self.animated:
            self.frame += self.frameStep

            if self.frame > self.lastFrame:
                self.frame = 0
