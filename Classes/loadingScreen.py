from functools import partial

from kivy import Logger
from kivy.clock import Clock

from Classes.screen import Screen


def bus_append(name, func, lastFunc, app, _):
    Logger.info("Loader: " + name)

    func()

    Clock.schedule_once(lastFunc, 0)


def switch(app):
    app.baseScreenManager.next()


class LoadingScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(LoadingScreen, self).__init__(*args, **kwargs)

        self.bus = list()
        self.app = None

        Logger.info("Application: Loading Screen setup")

    def start_bus(self, _):
        self.bus.reverse()

        i = 0
        last_func = lambda x: switch(self.app)

        for name, callback in self.bus:
            last_func = partial(bus_append, name, partial(callback, self.app), last_func, self.app)

            i += 1

        Clock.schedule_once(last_func, 0)
