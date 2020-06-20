from functools import partial

from kivy import Logger
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import *
from kivy.core.image import Image
from kivy.uix.progressbar import ProgressBar

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


        self.size = Window.size

        img = Image("textures/loadingScreenBackground.png").texture

        goOver = (Window.height * (img.width / img.height)) - Window.width

        with self.canvas:
            Rectangle(pos=(goOver / -2, 0),
                      size=(Window.height * (img.width /
                                             img.height), Window.height),
                      texture=img)



        self.progressBar = ProgressBar(max=10)


        Logger.info("Application: Loading Screen setup")



    def start_bus(self, _):
        self.bus.reverse()

        i = 0
        last_func = lambda x: switch(self.app)

        for name, callback in self.bus:
            last_func = partial(bus_append, name, partial(callback, self.app), last_func, self.app)

            i += 1

        Clock.schedule_once(last_func, 0)
