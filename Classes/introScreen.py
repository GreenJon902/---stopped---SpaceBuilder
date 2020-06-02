import math
import random
from io import BytesIO

from PIL import Image
from kivy import Logger
from kivy.animation import Animation
from kivy.core.image import Image as CoreImage
from kivy.clock import Clock
from kivy.graphics import *
from shapely import affinity
from shapely.geometry import LineString

from Classes.screen import Screen


class IntroScreen(Screen):
    def __init__(self, Globals, *args, **kwargs):
        super(IntroScreen, self).__init__(*args, **kwargs)
        self.starClock = None
        self.shipClock = None
        self.shakeClock = None
        self.meteorClock = None
        self.meteorClock2 = None
        self.tintClock = None
        self.tintClock2 = None
        self.Globals = Globals

        self.shakeScreenX = Globals.width / Globals.GameSettings.intro_ship_shake_amount_divider * -1
        self.shakeScreenY = Globals.height / Globals.GameSettings.intro_ship_shake_amount_divider * -1
        self.shakeDistanceX = self.shakeScreenX * -1
        self.shakeDistanceY = self.shakeScreenX * -1
        self.shakeScreenWidth = Globals.width - (self.shakeScreenX * 2)
        self.shakeScreenHeight = Globals.height - (self.shakeScreenY * 2)
        self.shipLayout = self.ids["ship"]
        self.starsLayout = self.ids["stars"]
        self.meteorLayout = self.ids["meteor"]
        self.tintLayout = self.ids["tint"]

        self.shipLayout.originX = Globals.width / 2
        self.shipLayout.originY = Globals.height / 2

        img = Image.open("textures/shipInside.png")
        width = img.size[0]
        height = img.size[1]

        ratio = self.shakeScreenHeight / self.shakeScreenWidth
        ratio2 = height / width

        takeAway = ratio - ratio2

        new_width = width - (width * takeAway)

        left = (width - new_width) / 2
        top = 0
        right = (width + new_width) / 2
        bottom = height

        img = img.crop((left, top, right, bottom))

        data = BytesIO()
        img.save(data, format='png')
        data.seek(0)
        self.shipImageTexture = CoreImage(BytesIO(data.read()), ext='png').texture

        img = Image.open("textures/star.png")

        data = BytesIO()
        img.save(data, format='png')
        data.seek(0)
        self.starImageTexture = CoreImage(BytesIO(data.read()), ext='png').texture

        Logger.info("Application: Intro Screen setup")

    def post_init(self):
        Logger.info("Application: Intro Screen entered")

        self.starClock = Clock.schedule_interval(self.draw_star, self.Globals.GameSettings.intro_star_new_frame_delay)
        self.shipClock = Clock.schedule_interval(self.draw_ship, self.Globals.GameSettings.intro_ship_new_frame_delay)
        self.meteorClock = Clock.schedule_once(self.start_draw_meteor, self.Globals.GameSettings.intro_meteor_delay)
        self.tintClock = Clock.schedule_once(self.start_alarm, self.Globals.GameSettings.intro_alarm_delay)
        self.shakeClock = Clock.schedule_once(self.shake, self.Globals.GameSettings.intro_ship_shake_delay)

        Logger.info("Application: Intro Screen clocks created")

    def draw_star(self, _):
        self.starsLayout.canvas.clear()

        Globals = self.Globals

        centerX, centerY = Globals.width / 2, Globals.height / 2
        width = Globals.width / Globals.GameSettings.intro_star_width_divider
        height = Globals.height / Globals.GameSettings.intro_star_height_divider

        cd_length = height

        for i in range(Globals.GameSettings.intro_star_amount):


            x, y = random.randint(0, Globals.width), random.randint(0, Globals.height / 2) + Globals.height / 2

            line = LineString([(centerX, centerY), (x, y)])
            left = line.parallel_offset(cd_length / 2, 'left')
            right = line.parallel_offset(cd_length / 2, 'right')
            p1 = left.boundary[1]
            p2 = right.boundary[0]

            x1, y1 = p1.coords[0]
            x2, y2 = p2.coords[0]

            a = 0, y1
            b = x1, y1
            c = x2, y2

            angle = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
            angle = angle + 360 if angle < 0 else angle

            rect = LineString([(x, y), (x, y + height), (x + width, y + height), (x + width, y)])
            rect = affinity.rotate(rect, angle + 90, "center")
            rect = rect.coords


            with self.starsLayout.canvas:
                Color(1, 1, 1)

                Mesh(indices=(0, 1, 2, 3),
                     vertices=(rect[0][0], rect[0][1], 0, 0, rect[1][0], rect[1][1], 0, 1,
                               rect[2][0], rect[2][1], 1, 1, rect[3][0], rect[3][1], 1, 0),
                     mode="triangle_fan", texture=self.starImageTexture)

    def start_draw_meteor(self, _):
        positions = self.Globals.GameSettings.intro_meteor_positions
        sizes = self.Globals.GameSettings.intro_meteor_positions
        size = self.Globals.width, self.Globals.height
        time1 = self.Globals.GameSettings.intro_meteor_length_1
        time2 = self.Globals.GameSettings.intro_meteor_length_2
        time3 = self.Globals.GameSettings.intro_meteor_length_3

        animation = Animation(center=(positions[0][0] * size[0], positions[0][1] * size[1]),
                              size=sizes[0], duration=time1)
        animation += Animation(center=(positions[1][0] * size[0], positions[1][1] * size[1]),
                               size=sizes[1], duration=time2)
        animation += Animation(pos=(positions[2][0] * size[0], positions[2][1] * size[1]),
                               size=sizes[2], duration=time3)
        animation.start(self.meteorLayout)

        self.meteorClock2 = Clock.schedule_interval(self.draw_meteor, 0)

        Logger.info("Application: Intro Screen meteor move started started")

    def draw_meteor(self, _):
        self.meteorLayout.canvas.clear()

        with self.meteorLayout.canvas:
            Rectangle(source="textures/meteor.png", pos=self.meteorLayout.pos, size=self.meteorLayout.size)


    def draw_ship(self, _):
        self.shipLayout.canvas.clear()

        with self.shipLayout.canvas:
            Rectangle(pos=(self.shakeScreenX + self.shipLayout.pos[0],
                           self.shakeScreenY + self.shipLayout.pos[1]),
                      size=(self.shakeScreenWidth, self.shakeScreenHeight),
                      texture=self.shipImageTexture)

    def shake(self, _):
        animation = Animation(pos=self.shipLayout.pos, duration=0)

        for pos in self.Globals.GameSettings.intro_ship_shake_positions:
            animation += Animation(pos=(self.shakeScreenX * pos[0], self.shakeScreenY * pos[1]),
                                   duration=self.Globals.GameSettings.intro_ship_shake_shake_length)

        animation += Animation(pos=(0, 0), duration=self.Globals.GameSettings.intro_ship_shake_shake_length)
        animation.start(self.shipLayout)

        Logger.info("Application: Intro Screen ship shake started")

    def start_alarm(self, _):
        self.tintClock2 = Clock.schedule_interval(self.do_alarm, self.Globals.GameSettings.intro_alarm_length * 2)
        Logger.info("Application: Intro Screen ship alarm stated")

    def do_alarm(self, _):
        with self.tintLayout.canvas:
            Rectangle(pos=(0, 0), size=(self.Globals.width, self.Globals.height),
                      color=Color(*self.Globals.GameSettings.intro_alarm_color))

        Clock.schedule_once(lambda _: self.tintLayout.canvas.clear(), self.Globals.GameSettings.intro_alarm_length)

    def on_leave(self, *args):
        Logger.info("Application: Intro Screen exited")

        self.starClock.cancel()
        self.shipClock.cancel()
        self.meteorClock2.cancel()
