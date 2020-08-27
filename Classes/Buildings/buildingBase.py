from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, StringProperty, DictProperty, BooleanProperty
from kivy.graphics import *

from Classes.globals import get_Globals


class BuildingBase(Widget, ButtonBehavior):
    rotation = NumericProperty(0)
    frame = NumericProperty(0)
    frameStep = NumericProperty(1)
    lastFrame = NumericProperty(0)
    name = StringProperty("BuildingBase")
    data = DictProperty({})
    animated = BooleanProperty(False)
    rotatable = BooleanProperty(False)

    def __init__(self, *args, **kwargs):
        super(BuildingBase, self).__init__(*args, **kwargs)
        self.Globals = get_Globals()

        self.bind(rotation=self.rotate)

    def rotate(self, _, rotation):
        with self.canvas.before:
            PushMatrix()
            Rotate(angle=rotation, origin=self.center)
        with self.canvas.after:
            PopMatrix()


    def draw(self):
        print(self.name, self.data, self.frame, self.animated)
        with self.canvas:
            Rectangle(pos=self.pos, size=(100, 100),
                      texture=self.Globals.BuildingTextures.get_texture(self.name, self.data, self.frame))

        if self.animated:
            self.frame += self.frameStep

            if self.frame > self.lastFrame:
                self.frame = 0
