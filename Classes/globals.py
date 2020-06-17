import json

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
            Logger.info("Application: App data save path: " + str(callback))

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
            Logger.info("Application: App data save path: " + str(callback))

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
        intro_ship_shake_repeats = 3
        intro_ship_shake_delay = 5
        intro_ship_shake_shake_length = 0.05
        intro_ship_new_frame_delay = 0.01
        intro_ship_shake_positions = ((0, 1), (0, 1))
        intro_alarm_color = 1, 0, 0, 0.5
        intro_alarm_delay = 5.1
        intro_alarm_length = 0.6
        intro_meteor_delay = 4
        intro_meteor_length_1 = 0
        intro_meteor_length_2 = 1
        intro_meteor_length_3 = 1
        intro_meteor_positions = ((0.75, 0.5), (0.1, 0.1), (0.5, 0.5))
        intro_meteor_sizes = ((0, 0), (1, 1), (0.1, 0.1))
        intro_move_delay = 10
        intro_move_speed = 1
        intro_end_delay = 11

        crash_move_delay = 0
        crash_move_length = 2
        crash_stars_move_divider = 3
        crash_guide_delay = 3
        crash_guide_speed = 1


    class _Textures:
        def __init__(self):
            canyon_surface = None
            canyon_surface_stars = None
            meteor = None
            guide_intro = None

        def load(self):
            self.canyon_surface = CoreImage("textures/canyon surface.png").texture
            self.canyon_surface_stars = CoreImage("textures/canyon surface stars.png").texture
            self.meteor = CoreImage("textures/meteor.png").texture
            self.guide_intro = CoreImage("textures/guide/intro.png").texture
