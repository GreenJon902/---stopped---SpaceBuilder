import json

from PIL import Image
from kivy.core.audio import SoundLoader
from kivy.core.image import Image as CoreImage
from kivy.event import EventDispatcher
from kivy.logger import Logger
from kivy.properties import StringProperty


class _Globals:
    width = 0
    height = 0

    def __init__(self):
        self.User_data = self._User_data()
        self.Settings_data = self._Settings_data()
        self.Textures = self._Textures()
        self.Audio = self._Audio()

    class _User_data(EventDispatcher):
        Default_data = {
            "introFinished": 0,
            "timesCrashed": 0,
            "layout": {}
        }

        save_path = StringProperty()
        data = {}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.bind(save_path=self.load)

        def load(self, _, callback):
            Logger.info("User_Data: Save path: " + str(callback))

            try:
                with open(callback, "r") as file:
                    self.data = json.load(file)

            except FileNotFoundError:
                Logger.warn("User_Data: Save file not found, creating new one")
                self.create_new()

                with open(callback, "r") as file:
                    self.data = json.load(file)

            Logger.info("User_Data: Loaded data")

        def _save(self, out):
            with open(self.save_path, "w", encoding='utf-8') as file:
                json.dump(out, file, ensure_ascii=True, indent=4)

            Logger.info("User_Data: Saved data")

        def save(self):
            self._save(self.data)

        def create_new(self):
            open(self.save_path, "a").close()
            Logger.info("User_Data: Created new data file")
            self._save(self.Default_data)

        def set(self, key, value):
            if key in self.data:
                self.data[key] = value

                Logger.info("User_Data: Set " + str(key) + " to " + str(value))

            else:
                Logger.warn("User_Data: \"" + str(key) + "\" is an invalid key")

        def get(self, key):
            if key in self.data:
                return self.data[key]

            else:
                Logger.warn("User_Data: \"" + str(key) + "\" is an invalid key")

    class _Settings_data(EventDispatcher):
        Default_data = {
            "buttonSize": 4
        }

        save_path = StringProperty()
        data = {}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.bind(save_path=self.load)

        def load(self, _, callback):
            Logger.info("Settings_Data: dave path: " + str(callback))

            try:
                with open(callback, "r") as file:
                    self.data = json.load(file)

            except FileNotFoundError:
                Logger.warn("Settings_Data: Save file not found, creating new one")
                self.create_new()

                with open(callback, "r") as file:
                    self.data = json.load(file)

            Logger.info("Settings_Data: Loaded data")

        def _save(self, out):
            with open(self.save_path, "w", encoding='utf-8') as file:
                json.dump(out, file, ensure_ascii=True, indent=4)

            Logger.info("Settings_Data: Saved data")

        def save(self):
            self._save(self.data)

        def create_new(self):
            open(self.save_path, "a").close()
            Logger.info("Settings_Data: Created new data file")
            self._save(self.Default_data)

        def set(self, key, value):
            if key in self.data:
                self.data[key] = value

                Logger.info("Settings_Data: Set " + str(key) + " to " + str(value))

            else:
                Logger.warn("Settings_Data: \"" + str(key) + "\" is an invalid key")

        def get(self, key):
            if key in self.data:
                return self.data[key]

            else:
                Logger.warn("Settings_Data: \"" + str(key) + "\" is an invalid key")

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
        intro_alarm_switch_interval = 0.6
        intro_alarm_sound_delay = 5
        intro_alarm_sound_interval = 1.2
        intro_alarm_sound_stop_delay = 9
        intro_meteor_delay = 4
        intro_meteor_length_times = (0, 0.25, 0.25, 0.25, 0.1)
        intro_meteor_positions = ((0.75, 0.5), (0.75, 0.5), (0.75, 0.5), (0.75, 0.5), (1.2, 1.2))
        intro_meteor_sizes = ((0, 0), (0.1, 0.1), (0.25, 0.25), (0.5, 0.5), (0.4, 0.4))
        intro_meteor_hit_sound_delay = 4.5
        intro_ship_fall_delay = 10
        intro_ship_fall_sound_delay = 10
        intro_ship_fall_speed = 1
        intro_end_delay = 11

        crash_move_delay = 0
        crash_move_length = 2
        crash_stars_move_divider = 3
        crash_guide_delay = 3
        crash_guide_speed = 1
        crash_click_1_delay = 4
        crash_click_transition_speed = 0.5

        base_builder_max_zoom = 10
        base_builder_min_zoom = 1
        base_builder_button_isBigger_amount = 2

    class _Textures:
        def __init__(self):
            self.cliff_edge = None
            self.cliff_edge_stars = None
            self.meteor = None
            self.guide_intro_1 = None
            self.guide_intro_2 = None
            self.ship_inside_1 = None
            self.ship_inside_2 = None
            self.star = None
            self.planetSurface = None
            self.build_button = None
            self.settings_button = None

        def load(self):
            self.cliff_edge = CoreImage("resources/textures/intro/cliffEdge.png").texture
            self.cliff_edge_stars = CoreImage("resources/textures/intro/cliffEdgeStars.png").texture
            self.meteor = CoreImage("resources/textures/intro/meteor.png").texture
            self.guide_intro_1 = CoreImage("resources/textures/guide/intro1.png").texture
            self.guide_intro_2 = CoreImage("resources/textures/guide/intro2.png").texture
            self.ship_inside_1 = Image.open("resources/textures/intro/shipInside1.png")
            self.ship_inside_2 = Image.open("resources/textures/intro/shipInside2.png")
            self.star = CoreImage("resources/textures/intro/star.png").texture
            self.planetSurface = CoreImage("resources/textures/baseBuilder/planetSurface.png").texture
            self.build_button = CoreImage("resources/textures/buttons/build.png").texture
            self.settings_button = CoreImage("resources/textures/buttons/settings.png").texture

    class _Audio:
        def __init__(self):
            self.meteorHit = None
            self.alarm = None
            self.shipFall = None

        def load(self):
            self.meteorHit = SoundLoader.load("resources/audio/intro/meteorHit.wav")
            self.alarm = SoundLoader.load("resources/audio/intro/alarm.wav")
            self.shipFall = SoundLoader.load("resources/audio/intro/shipFall.wav")


Globals = None


def init():
    global Globals
    Globals = _Globals()


def get_Globals():
    return Globals
