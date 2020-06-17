from functools import partial

from kivy import Logger
from kivy.clock import Clock

from Classes.screen import Screen


class LoadingScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(LoadingScreen, self).__init__(*args, **kwargs)

        self.bus = list()


    def start_bus(self, _):
        i = 0
        for vars in self.bus:
            name, callback, app = vars

            Logger.info("Loader: " + name)
            Clock.schedule_once(partial(callback, app), i)

            i += 1
