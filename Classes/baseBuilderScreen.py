from kivy import Logger
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen



class BaseBuilderScreen(Screen):
    def __init__(self, Globals, *args, **kwargs):
        super(BaseBuilderScreen, self).__init__(*args, **kwargs)
        self.drawClock = None

        self.Globals = Globals

        self.canyonFloorLayout = self.ids["canyonFloor"]
        self.buildingsLayout = self.ids["buildings"]
        self.canyonTopLayout = self.ids["canyonTop"]
        self.canyonDefencesLayout = self.ids["canyonDefences"]
        self.baseLayout = self.ids["base"]

        Logger.info("Application: BaseBuilder Screen setup")

    def post_init(self):
        Logger.info("Application: BaseBuilder Screen clocks created")

        self.drawClock = Clock.schedual_interval(self.draw, 0)

        Logger.info("Application: BaseBuilder Screen clocks created")

    def draw(self, _):
        self.canyonFloorLayout.canvas.clear()
        self.buildingsLayout.canvas.clear()
        self.canyonTopLayout.canvas.clear()

        with self.buildingsLayout.canvas:
            pass

        with self.canyonFloorLayout.canvas:
            pass

        with self.canyonTopLayout.canvas:
            pass

    def on_leave(self, *args):
        self.drawClock.cancel()

        Logger.info("Application: BaseBuilder Screen exited")
