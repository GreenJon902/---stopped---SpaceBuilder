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




        self.canyonFloorLayout.pos = 0, 0
        self.canyonFloorLayout.size = self.Globals.width, self.Globals.height

        self.buildingsLayout.pos = 0, 0
        self.buildingsLayout.size = self.Globals.width, self.Globals.height


        Logger.info("Application: BaseBuilder Screen setup")

    def post_init(self):
        Logger.info("Application: Intro Screen entered")

        self.drawClock = Clock.schedule_interval(self.draw, 0)

        Logger.info("Application: BaseBuilder Screen clocks created")


    def draw(self, _):
        self.canyonFloorLayout.canvas.clear()
        self.buildingsLayout.canvas.clear()
        self.canyonTopLayout.canvas.clear()

        with self.canyonFloorLayout.canvas:
            pass

        with self.buildingsLayout.canvas:
            pass


    def on_leave(self, *args):
        self.drawClock.cancel()

        Logger.info("Application: BaseBuilder Screen exited")
