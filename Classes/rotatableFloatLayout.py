from kivy.graphics import *
from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout


class RotatableFloatLayout(FloatLayout):
    angle = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super(RotatableFloatLayout, self).__init__(*args, **kwargs)

        with self.canvas.before:
            PushMatrix()
            self.rot = Rotate()
            self.rot.angle = 0
            self.rot.origin = self.center
            self.rot.axis = (0, 0, 1)

        with self.canvas.after:
            PopMatrix()
