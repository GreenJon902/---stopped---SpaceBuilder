from kivy import Logger
from kivy.uix.screenmanager import Screen



class BaseBuilderScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(BaseBuilderScreen, self).__init__(*args, **kwargs)

        Logger.info("Application: BaseBuilder Screen setup")

    def on_enter(self, *args):
        Logger.info("Application: BaseBuilder Screen entered")

    def on_leave(self, *args):
        Logger.info("Application: BaseBuilder Screen exited")
