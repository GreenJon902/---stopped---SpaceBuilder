import sys
import threading
from functools import partial

from kivy import Logger
from kivy.core.image import Image
from kivy.core.window import Window
from kivy.graphics import *
from kivy.uix.label import Label

from Classes.screen import Screen


def bus_append(name, func, lastFunc):
    Logger.info("Loader: " + name)

    func()

    lastFunc()


def switch(app):
    Logger.info("Loader: Loading Code")

    app.baseScreenManager.next()
    Logger.info("Loader: Stopping Loading Thread")
    print("heyyy", threading.get_ident(), threading.current_thread().name)
    sys.exit()


class LoadingScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(LoadingScreen, self).__init__(*args, **kwargs)

        self.bus = list()
        self.app = None




        self.size = Window.size

        img = Image("resources/textures/loadingScreenBackground.png").texture

        goOver = (Window.height * (img.width / img.height)) - Window.width

        with self.canvas:
            Rectangle(pos=(goOver / -2, 0),
                      size=(Window.height * (img.width /
                                             img.height), Window.height),
                      texture=img)


        self.label = Label(text="Loading", color=(1, 1, 1, 1),
                           font_size=Window.height / 10, font_name="resources/ComicSans.ttf")

        self.label.pos_hint = {"y": -0.25}

        self.add_widget(self.label)



        Logger.info("Application: Loading Screen setup")

    def start_bus(self, _=None):
        Logger.info("Loader: Starting Loading Thread")
        threading.Thread(target=self._start_bus, daemon=True, name="Loader").start()
        print("yhaaa", threading.get_ident(), threading.current_thread().name)


    def _start_bus(self):
        print("bdfs", threading.get_ident(), threading.current_thread().name)
        self.bus.reverse()

        i = 0
        last_func = partial(switch, self.app)

        for name, callback in self.bus:
            last_func = partial(bus_append, name, partial(callback, self.app), last_func)

            i += 1

        last_func()
