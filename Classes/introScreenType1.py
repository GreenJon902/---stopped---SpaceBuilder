import random

from kivy import Logger
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import *
from Classes.screen import Screen


class IntroScreenType1(Screen):
    def __init__(self, Globals, *args, **kwargs):
        super(IntroScreenType1, self).__init__(*args, **kwargs)
        self.starClock = None
        self.shipClock = None
        self.shakeClock = None
        self.tintClock = None
        self.tintClock2 = None
        self.rotateClock = None
        self.Globals = Globals

        self.shakeScreenX = Globals.width / Globals.GameSettings.intro_type_1_ship_shake_amount_divider * -1
        self.shakeScreenY = Globals.height / Globals.GameSettings.intro_type_1_ship_shake_amount_divider * -1
        self.shakeDistanceX = self.shakeScreenX * -1
        self.shakeDistanceY = self.shakeScreenX * -1
        self.shakeScreenWidth = Globals.width - (self.shakeScreenX * 2)
        self.shakeScreenHeight = Globals.height - (self.shakeScreenY * 2)
        self.starsLayout = None
        self.shipLayout = None
        self.tintLayout = None

        self.shipLayout.originX = Globals.width / 2
        self.shipLayout.originY = Globals.height / 2

        Logger.info("Application: Intro Screen setup")

    def post_init(self, _):
        self.starsLayout = self.ids["stars"]
        self.shipLayout = self.ids["ship"]
        self.tintLayout = self.ids["tint"]

    def on_enter(self, *args):
        Logger.info("Application: Intro Screen entered")

        self.starClock = Clock.schedule_interval(self.draw_star,
                                                 self.Globals.GameSettings.intro_type_1_star_new_frame_delay)
        self.shipClock = Clock.schedule_interval(self.draw_ship,
                                                 self.Globals.GameSettings.intro_type_1_ship_new_frame_delay)
        self.tintClock = Clock.schedule_once(self.start_alarm, self.Globals.GameSettings.intro_type_1_alarm_delay)
        self.shakeClock = Clock.schedule_once(self.shake, self.Globals.GameSettings.intro_type_1_ship_shake_delay)
        self.rotateClock = Clock.schedule_once(self.rotate, self.Globals.GameSettings.intro_type_1_ship_rotate_delay)

        Logger.info("Application: Intro Screen clocks created")

    def draw_star(self, _):
        self.starsLayout.canvas.clear()

        Globals = self.Globals

        for i in range(Globals.GameSettings.intro_type_1_star_amount):
            with self.starsLayout.canvas:
                Color(1, 1, 1)

                x, y = random.randint(0, Globals.width), random.randint(0, Globals.height / 2) + Globals.height / 2

                Rectangle(pos=(x, y), size=(Globals.width / Globals.GameSettings.intro_type_1_star_width_divider,
                                            Globals.height / Globals.GameSettings.intro_type_1_star_height_divider))

    def draw_ship(self, _):
        self.shipLayout.canvas.clear()

        with self.shipLayout.canvas:
            Rectangle(pos=(self.shakeScreenX + self.shipLayout.pos[0],
                           self.shakeScreenY + self.shipLayout.pos[1]), size=(self.shakeScreenWidth,
                                                                              self.shakeScreenHeight),
                      source="textures/shipInside.png")

    def shake(self, _):
        animation = Animation(pos=self.shipLayout.pos, duration=0)

        for pos in self.Globals.GameSettings.intro_type_1_ship_shake_positions:
            animation += Animation(pos=(self.shakeScreenX * pos[0], self.shakeScreenY * pos[1]),
                                   duration=self.Globals.GameSettings.intro_type_1_ship_shake_shake_length)

        animation += Animation(pos=(0, 0), duration=self.Globals.GameSettings.intro_type_1_ship_shake_shake_length)
        animation.start(self.shipLayout)

        Logger.info("Application: Intro Screen ship shake started")

    def start_alarm(self, _):
        self.tintClock2 = Clock.schedule_interval(self.do_alarm, self.Globals.GameSettings.intro_type_1_alarm_length * 2)
        Logger.info("Application: Intro Screen ship alarm stated")

    def do_alarm(self, _):
        with self.tintLayout.canvas:
            Rectangle(pos=(0, 0), size=(self.Globals.width, self.Globals.height),
                      color=Color(*self.Globals.GameSettings.intro_type_1_alarm_color))

        Clock.schedule_once(lambda _: self.tintLayout.canvas.clear(), self.Globals.GameSettings.intro_type_1_alarm_length)

    def rotate(self, _):
        animation = Animation(angle=self.shipLayout.angle, duration=0)
        animation += Animation(angle=self.Globals.GameSettings.intro_type_1_ship_rotate_degrees,
                               duration=self.Globals.GameSettings.intro_type_1_ship_rotate_length)

        animation.start(self.shipLayout)


    def on_leave(self, *args):
        Logger.info("Application: Intro Screen exited")

        self.starClock.cancel()
        self.shipClock.cancel()
