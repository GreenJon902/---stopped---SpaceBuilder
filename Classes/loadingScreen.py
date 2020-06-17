from functools import partial

from kivy import Logger
from kivy.clock import Clock

from Classes.screen import Screen


def bus_append(name, func, lastFunc, i):
    Logger.info("Loader: " + name)

    func()

    Clock.schedule_once(lastFunc, i)


class LoadingScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(LoadingScreen, self).__init__(*args, **kwargs)

        self.bus = list()
        self.app = None
        self.nextWidget = None


    def start_bus(self, _):
        self.bus.reverse()
        
        i = 0
        last_func = print

        for vars in self.bus:
            name, callback, app = vars

            func = callback

            um = partial(bus_append, name, func, last_func, i)

            last_func = func

            Clock.schedule_once()

            i += 1
