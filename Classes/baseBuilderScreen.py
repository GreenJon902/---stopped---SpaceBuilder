from kivy import Logger

from Classes.globals import get_Globals
from Classes.screen import Screen


class BaseBuilderScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(BaseBuilderScreen, self).__init__(*args, **kwargs)

        self.Globals = get_Globals()

        self.baseBuilderHolder = self.ids["baseBuilderHolder"]
        self.baseBuilder = self.ids["baseBuilder"]

        self.baseBuilderHolder.pos = 0, 0
        self.baseBuilderHolder.size = self.Globals.width, self.Globals.height


        Logger.info("Application: BaseBuilder Screen setup")

    def post_init(self):
        Logger.info("Application: Intro Screen entered")

    def on_leave(self, *args):
        Logger.info("Application: BaseBuilder Screen exited")
