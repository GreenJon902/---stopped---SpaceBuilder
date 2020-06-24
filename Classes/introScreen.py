import math
import random
from io import BytesIO

from kivy import Logger
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from kivy.graphics import *
from shapely import affinity
from shapely.geometry import LineString

from Classes.screen import Screen


class IntroScreen(Screen):
    def __init__(self, Globals, *args, **kwargs):
        super(IntroScreen, self).__init__(*args, **kwargs)
        self.starClock = None
        self.shipClock = None
        self.shipShakeClock = None
        self.meteorHitSoundClock = None
        self.meteorClock = None
        self.meteorClock2 = None
        self.tintClock = None
        self.tintClock2 = None
        self.alarmSoundClock = None
        self.alarmSoundClock2 = None
        self.alarmSoundStopClock = None
        self.shipFallClock = None
        self.shipFallSoundClock = None
        self.endClock = None

        self.Globals = Globals

        self.shakeScreenX = self.Globals.width / self.Globals.GameSettings.intro_ship_shake_amount_divider * -1
        self.shakeScreenY = self.Globals.height / self.Globals.GameSettings.intro_ship_shake_amount_divider * -1
        self.shakeDistanceX = self.shakeScreenX * -1
        self.shakeDistanceY = self.shakeScreenX * -1
        self.shakeScreenWidth = Globals.width - (self.shakeScreenX * 2)
        self.shakeScreenHeight = Globals.height - (self.shakeScreenY * 2)
        self.shipLayout = self.ids["ship"]
        self.starsLayout = self.ids["stars"]
        self.meteorLayout = self.ids["meteor"]
        self.tintLayout = self.ids["tint"]

        self.meteorLayout.size = (0, 0)
        self.meteorLayout.size_hint = (None, None)

        self.shipLayout.originX = self.Globals.width / 2
        self.shipLayout.originY = self.Globals.height / 2

        img = Globals.Textures.ship_inside_1
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
        self.shipImageTexture1 = CoreImage(BytesIO(data.read()), ext='png').texture

        img = Globals.Textures.ship_inside_2
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
        self.shipImageTexture2 = CoreImage(BytesIO(data.read()), ext='png').texture

        self.shipImageTexture = self.shipImageTexture1


        Logger.info("Application: Intro Screen setup")

    def post_init(self):
        Logger.info("Application: Intro Screen entered")

        self.starClock = Clock.schedule_interval(self.draw_star, self.Globals.GameSettings.intro_star_new_frame_delay)
        self.shipClock = Clock.schedule_interval(self.draw_ship, self.Globals.GameSettings.intro_ship_new_frame_delay)
        self.meteorClock = Clock.schedule_once(self.move_meteor, self.Globals.GameSettings.intro_meteor_delay)
        self.meteorClock2 = Clock.schedule_interval(self.draw_meteor, 0)
        self.meteorHitSoundClock = Clock.schedule_once(lambda x: self.Globals.Audio.meteorHit.play(),
                                                       self.Globals.GameSettings.intro_meteor_hit_sound_delay)
        self.tintClock = Clock.schedule_once(self.start_alarm, self.Globals.GameSettings.intro_alarm_delay)
        self.alarmSoundClock = Clock.schedule_once(lambda x: self.alarmSoundClock2.cancel(),
                                                   self.Globals.GameSettings.intro_alarm_sound_stop_delay)
        self.alarmSoundClock = Clock.schedule_once(self.start_alarm_sounds,
                                                   self.Globals.GameSettings.intro_alarm_sound_delay)
        self.shipShakeClock = Clock.schedule_once(self.shake, self.Globals.GameSettings.intro_ship_shake_delay)
        self.shipFallClock = Clock.schedule_once(self.move, self.Globals.GameSettings.intro_ship_fall_delay)
        self.shipFallSoundClock = Clock.schedule_once(lambda x: self.Globals.Audio.shipFall.play(),
                                                      self.Globals.GameSettings.intro_ship_fall_sound_delay)
        self.endClock = Clock.schedule_once(self.parent.openCrashScreen, self.Globals.GameSettings.intro_end_delay)




        Logger.info("Application: Intro Screen clocks created")

    def start_alarm_sounds(self, _):
        self.alarmSoundClock2 = Clock.schedule_interval(lambda x: self.Globals.Audio.alarm.play(),
                                                        self.Globals.GameSettings.intro_alarm_sound_interval)

    def move(self, _):
        Logger.info("Application: Intro Screen ship move started")

        self.shipImageTexture = self.shipImageTexture2

        animation = Animation(pos=self.shipLayout.pos, duration=0)
        animation += Animation(pos=(self.shipLayout.pos[0], self.shakeScreenHeight * -1),
                               duration=self.Globals.GameSettings.intro_ship_fall_speed)

        animation.start(self.shipLayout)

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
                     mode="triangle_fan", texture=self.Globals.Textures.star)

    def move_meteor(self, _):
        positions = self.Globals.GameSettings.intro_meteor_positions
        sizes = self.Globals.GameSettings.intro_meteor_sizes
        winSize = self.Globals.width, self.Globals.height
        times = self.Globals.GameSettings.intro_meteor_length_times

        animation = Animation(duration=0)

        for i in range(len(times)):
            pos = (positions[i][0] * winSize[0], positions[i][1] * winSize[1])
            size = (sizes[i][0] * winSize[0], sizes[i][1] * winSize[0])

            animation += Animation(center=pos, size=size, duration=times[i])

        animation.start(self.meteorLayout)

        Logger.info("Application: Intro Screen meteor move started")

    def draw_meteor(self, _):
        self.meteorLayout.canvas.clear()

        with self.meteorLayout.canvas:
            Rectangle(texture=self.Globals.Textures.meteor, pos=self.meteorLayout.pos, size=self.meteorLayout.size)


    def draw_ship(self, _):
        self.shipLayout.canvas.clear()

        with self.shipLayout.canvas:
            Rectangle(pos=(self.shakeScreenX + self.shipLayout.pos[0],
                           self.shakeScreenY + self.shipLayout.pos[1]),
                      size=(self.shakeScreenWidth, self.shakeScreenHeight),
                      texture=self.shipImageTexture)

    def shake(self, _):
        animation = Animation(pos=self.shipLayout.pos, duration=0)

        i = 0

        for pos in self.Globals.GameSettings.intro_ship_shake_positions:
            animation += Animation(pos=(self.shakeScreenX * pos[0], self.shakeScreenY * pos[1]),
                                   duration=self.Globals.GameSettings.intro_ship_shake_shake_length_times[i])

            i = i + 1

        animation += Animation(pos=(0, 0), duration=self.Globals.GameSettings.intro_ship_shake_shake_length_times[i])
        animation.start(self.shipLayout)

        Logger.info("Application: Intro Screen ship shake started")

    def start_alarm(self, _):
        self.tintClock2 = Clock.schedule_interval(self.do_alarm,
                                                  self.Globals.GameSettings.intro_alarm_switch_interval * 2)
        Logger.info("Application: Intro Screen ship alarm stated")

    def do_alarm(self, _):
        with self.tintLayout.canvas:
            Rectangle(pos=(0, 0), size=(self.Globals.width, self.Globals.height),
                      color=Color(*self.Globals.GameSettings.intro_alarm_color))

        Clock.schedule_once(lambda _: self.tintLayout.canvas.clear(),
                            self.Globals.GameSettings.intro_alarm_switch_interval)

    def on_leave(self, *args):
        Logger.info("Application: Intro Screen exited")

        self.starClock.cancel()
        self.shipClock.cancel()
