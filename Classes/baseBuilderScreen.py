from kivy import Logger
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen



class BaseBuilderScreen(Screen):
    def __init__(self, Globals, *args, **kwargs):
        super(BaseBuilderScreen, self).__init__(*args, **kwargs)
        self.drawClock = None

        self.Globals = Globals

        Logger.info("Application: BaseBuilder Screen setup")

    def post_init(self):
        Logger.info("Application: BaseBuilder Screen clocks created")

        self.drawClock = Clock.schedual_interval(self.draw, 0)

        Logger.info("Application: BaseBuilder Screen clocks created")

    def on_leave(self, *args):
        Logger.info("Application: BaseBuilder Screen exited")
