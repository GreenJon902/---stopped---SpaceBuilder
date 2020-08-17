from kivy import Logger
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import *

from Classes.globals import get_Globals
from Classes.screen import Screen


class CrashScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(CrashScreen, self).__init__(*args, **kwargs)

        self.Globals = get_Globals()

        self.canyonClock = None
        self.starClock = None
        self.drawClock = None
        self.guideClock = None
        self.click1Clock = None

        self.starLayout = None
        self.canyonLayout = None
        self.guideLayout1 = None
        self.guideLayout2 = None

        self.currentClick = 0

        ratio = self.Globals.Textures.cliff_edge_stars.width / self.Globals.Textures.cliff_edge_stars.height
        self.h = self.Globals.height
        self.w = ratio * self.h

        Logger.info("Application: IntroCrash Screen vars setup")

    def post_init(self):
        self.starLayout = self.ids["stars"]
        self.canyonLayout = self.ids["canyon"]
        self.guideLayout1 = self.ids["guide1"]
        self.guideLayout2 = self.ids["guide2"]

        self.starLayout.pos = (self.Globals.width, 0)
        self.canyonLayout.pos = (self.Globals.width, 0)
        self.guideLayout1.pos = (self.Globals.width * -1, 0)

        self.guideLayout2.opacity = 0

        Logger.info("Application: IntroCrash Screen widgets setup")

    def post_enter(self):
        Logger.info("Application: IntroCrash Screen entered")

        self.canyonClock = Clock.schedule_once(self.move_canyon, self.Globals.GameSettings.intro_crash_move_delay)
        self.starClock = Clock.schedule_once(self.move_stars, self.Globals.GameSettings.intro_crash_move_delay)
        self.drawClock = Clock.schedule_interval(self.draw, 0)
        self.guideClock = Clock.schedule_once(self.guide_move, self.Globals.GameSettings.intro_crash_guide_delay)
        self.click1Clock = Clock.schedule_once(self.click1allow, self.Globals.GameSettings.intro_crash_click_1_delay)

    def click1allow(self, _=None):
        self.currentClick = 1

    def on_touch_up(self, _=None):
        if self.currentClick == 1:

            animation1 = Animation(opacity=1, duration=0)
            animation1 += Animation(opacity=0, duration=self.Globals.GameSettings.intro_crash_click_transition_speed)

            animation2 = Animation(opacity=0, duration=0)
            animation2 += Animation(opacity=1, duration=self.Globals.GameSettings.intro_crash_click_transition_speed)

            animation1.start(self.guideLayout1)
            animation2.start(self.guideLayout2)

            self.currentClick = 2

        elif self.currentClick == 2:
            self.Globals.get_screen_manager().sendTo("BaseBuilderScreen")


    def move_canyon(self, _=None):
        Logger.info("Application: IntroCrash Screen canyon move started")

        animation = Animation(pos=self.canyonLayout.pos, duration=0)
        animation += Animation(pos=((self.w * -1) + self.Globals.width, self.canyonLayout.pos[1]),
                               duration=self.Globals.GameSettings.intro_crash_move_length)

        animation.start(self.canyonLayout)

    def guide_move(self, _=None):
        Logger.info("Application: IntroCrash Screen guide move started")

        animation = Animation(pos=self.guideLayout1.pos, duration=0)
        animation += Animation(pos=(0, 0),
                               duration=self.Globals.GameSettings.intro_crash_guide_speed)

        animation.start(self.guideLayout1)


    def move_stars(self, _=None):
        Logger.info("Application: IntroCrash Screen stars move started")

        animation = Animation(pos=self.starLayout.pos, duration=0)
        animation += Animation(pos=(((self.w * -1) + self.Globals.width) /
                                    self.Globals.GameSettings.intro_crash_stars_move_divider, self.starLayout.pos[1]),
                               duration=self.Globals.GameSettings.intro_crash_move_length)

        animation.start(self.starLayout)

    def draw(self, _=None):
        self.starLayout.canvas.clear()
        self.canyonLayout.canvas.clear()
        self.guideLayout1.canvas.clear()
        self.guideLayout2.canvas.clear()

        with self.starLayout.canvas:
            Rectangle(pos=self.starLayout.pos, size=(self.w, self.h),
                      texture=self.Globals.Textures.cliff_edge_stars)

        with self.canyonLayout.canvas:
            Rectangle(pos=self.canyonLayout.pos, size=(self.w, self.h),
                      texture=self.Globals.Textures.cliff_edge)

        with self.guideLayout1.canvas:
            Rectangle(pos=self.guideLayout1.pos,
                      size=(self.Globals.height * (self.Globals.Textures.guide_intro_1.width /
                                                   self.Globals.Textures.guide_intro_1.height), self.Globals.height),
                      texture=self.Globals.Textures.guide_intro_1,
                      color=Color(1, 1, 1))

        with self.guideLayout2.canvas:
            Rectangle(pos=self.guideLayout1.pos,
                      size=(self.Globals.height * (self.Globals.Textures.guide_intro_2.width /
                                                   self.Globals.Textures.guide_intro_2.height), self.Globals.height),
                      texture=self.Globals.Textures.guide_intro_2,
                      color=Color(1, 1, 1))

    def on_leave(self, *args):
        self.Globals.User_data.set("introFinished", 1)
