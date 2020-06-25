from kivy import Logger
from kivy.clock import Clock
from kivy.graphics import *
from kivy.uix.widget import Widget

from Classes.screen import Screen


class BaseBuilderScreen(Screen):
    def __init__(self, Globals, *args, **kwargs):
        super(BaseBuilderScreen, self).__init__(*args, **kwargs)
        self.drawClock = None

        self.pos2 = 0, 0
        self.size2 = 100, 100
        self.Globals = Globals

        self.canyonBackgroundLayout = self.ids["canyonBackground"]
        self.buildingsLayout = self.ids["buildings"]
        self.canyonDefencesLayout = self.ids["canyonDefences"]
        self.sizeAndPositionLayout = self.ids["sizeAndPosition"]

        ratio = Globals.Textures.canyon_background.width / Globals.Textures.canyon_background.height
        self.sizeAndPositionLayout.add_widget(Widget(pos=(0, 0),
                                                     size=(self.Globals.height * ratio, self.Globals.height)))
        self.sizeAndPositionLayout.min_scale = 1
        self.sizeAndPositionLayout.bind(on_transform_with_touch=self.zoomOrMove)
        self.zoomOrMove()

        self.sizeAndPositionLayout.pos = 0, 0
        self.sizeAndPositionLayout.size = self.Globals.width, self.Globals.height

        self.canyonBackgroundLayout.pos = 0, 0
        self.canyonBackgroundLayout.size = self.Globals.width, self.Globals.height

        self.buildingsLayout.pos = 0, 0
        self.buildingsLayout.size = self.Globals.width, self.Globals.height

        self.canyonDefencesLayout.pos = 0, 0
        self.canyonDefencesLayout.size = self.Globals.width, self.Globals.height

        Logger.info("Application: BaseBuilder Screen setup")



    def post_init(self):
        Logger.info("Application: Intro Screen entered")

        self.drawClock = Clock.schedule_interval(self.draw, 0)

        Logger.info("Application: BaseBuilder Screen clocks created")

    def zoomOrMove(self, _=None, x=None):
        self.pos2 = self.sizeAndPositionLayout.pos

        ratio = self.Globals.Textures.canyon_background.width / \
            self.Globals.Textures.canyon_background.height
        self.size2 = self.Globals.height * ratio * self.sizeAndPositionLayout.scale, \
            self.Globals.height * self.sizeAndPositionLayout.scale


    def draw(self, _):
        self.canyonBackgroundLayout.canvas.before.clear()
        self.buildingsLayout.canvas.before.clear()
        self.canyonDefencesLayout.canvas.before.clear()

        with self.canyonBackgroundLayout.canvas.before:
            Rectangle(pos=self.pos2, size=self.size2,
                      texture=self.Globals.Textures.canyon_background)

        with self.buildingsLayout.canvas.before:
            pass

        with self.canyonDefencesLayout.canvas.before:
            pass

    def on_leave(self, *args):
        self.drawClock.cancel()

        Logger.info("Application: BaseBuilder Screen exited")
