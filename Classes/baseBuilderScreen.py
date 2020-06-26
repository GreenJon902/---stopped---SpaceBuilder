from kivy import Logger

from Classes.screen import Screen


class BaseBuilderScreen(Screen):
    def __init__(self, Globals, *args, **kwargs):
        super(BaseBuilderScreen, self).__init__(*args, **kwargs)

        self.Globals = Globals


        self.sizeAndPositionLayout = self.ids["sizeAndPosition"]

        self.sizeAndPositionLayout.pos = 0, 0
        self.sizeAndPositionLayout.size = self.Globals.width, self.Globals.height


        Logger.info("Application: BaseBuilder Screen setup")

    def post_init(self):
        Logger.info("Application: Intro Screen entered")

    def on_leave(self, *args):
        Logger.info("Application: BaseBuilder Screen exited")
