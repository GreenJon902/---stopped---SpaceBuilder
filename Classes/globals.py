import json

from PIL import Image
from kivy.core.audio import SoundLoader
from kivy.core.image import Image as CoreImage
from kivy.event import EventDispatcher
from kivy.logger import Logger
from kivy.properties import StringProperty


class Globals:
    width = 0
    height = 0

    def __init__(self):
        self.User_data = self._User_data()
        self.Settings_data = self._Settings_data()
        self.Textures = self._Textures()
        self.Audio = self._Audio()

    class _User_data(EventDispatcher):
        Default_data = {
            "intoFinished": 0,
            "timesCrashed": 0,
            "layout": {}
        }

        save_path = StringProperty()
        data = {}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.bind(save_path=self.load)

        def load(self, _, callback):
            Logger.info("Application: User data save path: " + str(callback))

            try:
                with open(callback, "r") as file:
                    self.data = json.load(file)

            except FileNotFoundError:
                Logger.warn("Application: User data save file not found, creating new one")
                self.create_new()

                with open(callback, "r") as file:
                    self.data = json.load(file)

            Logger.info("Application: Loaded user data")

        def save(self, out):
            with open(self.save_path, "w", encoding='utf-8') as file:
                json.dump(out, file, ensure_ascii=True, indent=4)

            Logger.info("Application: Saved user data")

        def create_new(self):
            open(self.save_path, "a").close()
            Logger.info("Application: Created new user data file")
            self.save(self.Default_data)

        def set(self, key, value):
            if key in self.data:
                self.data[key] = value

            else:
                Logger.warn("Application: \"" + str(key) + "\" is an invalid key for User data")

        def get(self, key):
            if key in self.data:
                return self.data[key]

            else:
                Logger.warn("Application: \"" + str(key) + "\" is an invalid key for User data")

    class _Settings_data(EventDispatcher):
        Default_data = {
            "buttonSize": 10
        }

        save_path = StringProperty()
        data = {}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.bind(save_path=self.load)

        def load(self, _, callback):
            Logger.info("Application: Settings data save path: " + str(callback))

            try:
                with open(callback, "r") as file:
                    self.data = json.load(file)

            except FileNotFoundError:
                Logger.warn("Application: Settings data save file not found, creating new one")
                self.create_new()

                with open(callback, "r") as file:
                    self.data = json.load(file)

            Logger.info("Application: Loaded settings data")

        def save(self, out):
            with open(self.save_path, "w", encoding='utf-8') as file:
                json.dump(out, file, ensure_ascii=True, indent=4)

            Logger.info("Application: Saved settings data")

        def create_new(self):
            open(self.save_path, "a").close()
            Logger.info("Application: Created new settings data file")
            self.save(self.Default_data)

        def set(self, key, value):
            if key in self.data:
                self.data[key] = value

            else:
                Logger.warn("Application: \"" + str(key) + "\" is an invalid key for Settings data")

        def get(self, key):
            if key in self.data:
                return self.data[key]

            else:
                Logger.warn("Application: \"" + str(key) + "\" is an invalid key for Settings data")

    class GameSettings:
        intro_star_amount = 10
        intro_star_width_divider = 10
        intro_star_height_divider = 100
        intro_star_new_frame_delay = 0.1
        intro_ship_shake_amount_divider = 5
        intro_ship_shake_delay = 4.75
        intro_ship_shake_shake_length_times = (0.1, 0.05, 0.1)
        intro_ship_new_frame_delay = 0.01
        intro_ship_shake_positions = ((1, 0.5), (1, 0.5))
        intro_alarm_color = 1, 0, 0, 0.5
        intro_alarm_delay = 5.1
        intro_alarm_length = 0.6
        intro_meteor_delay = 4
        intro_meteor_length_times = (0, 0.25, 0.25, 0.25, 0.1)
        intro_meteor_positions = ((0.75, 0.5), (0.75, 0.5), (0.75, 0.5), (0.75, 0.5), (1.2, 1.2))
        intro_meteor_sizes = ((0, 0), (0.1, 0.1), (0.25, 0.25), (0.5, 0.5), (0.4, 0.4))
        intro_move_delay = 10
        intro_move_speed = 1
        intro_end_delay = 11

        crash_move_delay = 0
        crash_move_length = 2
        crash_stars_move_divider = 3
        crash_guide_delay = 3
        crash_guide_speed = 1
        crash_click_1_delay = 4
        crash_click_transition_speed = 0.5


    class _Textures:
        def __init__(self):
            self.canyon_surface = None
            self.canyon_surface_stars = None
            self.meteor = None
            self.guide_intro1 = None
            self.guide_intro2 = None
            self.ShipInside1 = None
            self.ShipInside2 = None
            self.star = None

        def load(self):
            self.canyon_surface = CoreImage("resources/textures/intro/canyonSurface.png").texture
            self.canyon_surface_stars = CoreImage("resources/textures/intro/canyonSurfaceStars.png").texture
            self.meteor = CoreImage("resources/textures/intro/meteor.png").texture
            self.guide_intro1 = CoreImage("resources/textures/guide/intro1.png").texture
            self.guide_intro2 = CoreImage("resources/textures/guide/intro2.png").texture
            self.ShipInside1 = Image.open("resources/textures/intro/shipInside1.png")
            self.ShipInside2 = Image.open("resources/textures/intro/shipInside2.png")
            self.star = Image.open("resources/textures/intro/star.png")

    class _Audio:
        def __init__(self):
            self.meteorHit = None
            self.alarm = None
            self.shipFall = None

        def load(self):
            self.meteorHit = SoundLoader.load("resources/audio/intro/meteorHit.wav")
            self.alarm = SoundLoader.load("resources/audio/intro/alarm.wav")
            self.shipFall = SoundLoader.load("resources/audio/intro/shipFall.wav")
