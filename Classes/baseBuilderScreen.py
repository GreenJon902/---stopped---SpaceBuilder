from kivy import Logger
from kivy.uix.screenmanager import Screen



class BaseBuilderScreen(Screen):
    def __init__(self, Globals, *args, **kwargs):
        super(BaseBuilderScreen, self).__init__(*args, **kwargs)

        self.Globals = Globals

        Logger.info("Application: BaseBuilder Screen setup")

    def on_enter(self, *args):
        Logger.info("Application: BaseBuilder Screen entered")

    def on_leave(self, *args):
        Logger.info("Application: BaseBuilder Screen exited")
