from kivy import Logger

from Classes.globals import get_Globals
from Classes.screen import Screen


class BaseBuilderScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(BaseBuilderScreen, self).__init__(*args, **kwargs)

        self.Globals = get_Globals()

        self.baseBuilder = None
        self.baseBuilderHolder = None


        Logger.info("Application: BaseBuilder Screen vars setup")

    def post_enter(self):
        Logger.info("Application: BaseBuilder Screen entered")

    def post_init(self):
        self.baseBuilderHolder = self.ids["baseBuilderHolder"]
        self.baseBuilder = self.ids["baseBuilder"]

        self.baseBuilderHolder.pos = 0, 0
        self.baseBuilderHolder.size = self.Globals.width, self.Globals.height

        self.baseBuilderHolder.scale_min = self.Globals.GameSettings.base_builder_min_zoom
        self.baseBuilderHolder.scale_max = self.Globals.GameSettings.base_builder_max_zoom
        self.baseBuilderHolder.scale = self.Globals.GameSettings.base_builder_default_zoom

        self.baseBuilder.center = self.baseBuilderHolder.center

        Logger.info("Application: BaseBuilder Screen widgets setup")

    def on_leave(self, *args):
        Logger.info("Application: BaseBuilder Screen exited")
