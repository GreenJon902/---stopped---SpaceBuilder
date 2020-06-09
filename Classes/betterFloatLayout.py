from kivy.graphics import *
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.floatlayout import FloatLayout


class BetterFloatLayout(FloatLayout):
    angle = NumericProperty(0)
    originX = NumericProperty(0)
    originY = NumericProperty(0)

    color = ListProperty([0, 0, 0, 0])

    def __init__(self, *args, **kwargs):
        super(BetterFloatLayout, self).__init__(*args, **kwargs)

        self.bind(angle=self.rotate)
        self.bind(color=self.colorChange)

        with self.canvas.before:
            PushMatrix()
            self.rot = Rotate()
            self.rot.angle = 0
            self.rot.axis = (0, 0, 1)

        with self.canvas.after:
            PopMatrix()


    def rotate(self, _, instance):
        print(instance)

        with self.canvas.before:
            PushMatrix()
            self.rot.origin = self.originX, self.originY
            self.rot.angle = instance

        with self.canvas.after:
            PopMatrix()

    def colorChange(self, _, color):
        with self.canvas.before:
            Color(color)
            Rectangle(pos=self.pos, size=self.size)
