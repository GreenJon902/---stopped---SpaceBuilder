from kivy import Logger
from kivy.clock import Clock
from kivy.graphics import *

from Classes.screen import Screen



class BaseBuilderScreen(Screen):
    def __init__(self, Globals, *args, **kwargs):
        super(BaseBuilderScreen, self).__init__(*args, **kwargs)
        self.drawClock = None

        self.Globals = Globals

        self.canyonFloorLayout = self.ids["canyonFloor"]
        self.buildingsLayout = self.ids["buildings"]
        self.canyonTopLayout = self.ids["canyonTop"]
        self.canyonDefencesLayout = self.ids["canyonDefences"]
        self.sizeAndPositionLayout = self.ids["sizeAndPosition"]

        self.sizeAndPositionLayout.bind(on_transform_with_touch=self.zoomOrMove)


        ratio = Globals.Textures.canyon_background_bottom.width / Globals.Textures.canyon_background_bottom.height
        self.sizeAndPositionLayout.size = self.Globals.height * ratio, self.Globals.height

        self.canyonFloorLayout.pos = 0, 0
        self.canyonFloorLayout.size = self.sizeAndPositionLayout.size

        self.buildingsLayout.pos = 0, 0
        self.buildingsLayout.size = self.sizeAndPositionLayout.size

        self.canyonTopLayout.pos = 0, 0
        self.canyonTopLayout.size = self.sizeAndPositionLayout.size

        self.canyonDefencesLayout.pos = 0, 0
        self.canyonDefencesLayout.size = self.sizeAndPositionLayout.size


        Logger.info("Application: BaseBuilder Screen setup")

    def post_init(self):
        Logger.info("Application: Intro Screen entered")

        self.drawClock = Clock.schedule_interval(self.draw, 0)

        Logger.info("Application: BaseBuilder Screen clocks created")

    def zoomOrMove(self, _=None, x=None):
        print(self.sizeAndPosition.pos)
        print(self.sizeAndPosition.size)

    def draw(self, _):
        self.canyonFloorLayout.canvas.clear()
        self.buildingsLayout.canvas.clear()
        self.canyonTopLayout.canvas.clear()

        with self.canyonFloorLayout.canvas:
            Rectangle(pos=self.canyonFloorLayout.pos, size=self.canyonFloorLayout.size,
                      texture=self.Globals.Textures.canyon_background_bottom)

        with self.buildingsLayout.canvas:
            pass

        with self.canyonTopLayout.canvas:
            Rectangle(pos=self.canyonTopLayout.pos, size=self.canyonTopLayout.size,
                      texture=self.Globals.Textures.canyon_background_top)

    def on_leave(self, *args):
        self.drawClock.cancel()

        Logger.info("Application: BaseBuilder Screen exited")
