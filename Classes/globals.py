import json
import os

from PIL import Image
from kivy.core.audio import SoundLoader
from kivy.core.image import Image as CoreImage
from kivy.event import EventDispatcher
from kivy.properties import StringProperty
from kivy.logger import Logger



class _user_and_settings_data_base(EventDispatcher):
    Default_data = {}
    save_path = StringProperty()
    data = {}
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bind(save_path=self.load)

    def load(self, _, callback):
        Logger.info(self.name + ": Save path: " + str(callback))

        try:
            with open(callback, "r") as file:
                self.data = json.load(file)

        except FileNotFoundError:
            Logger.warn(self.name + ": Save file not found, creating new one")
            self.create_new()

            with open(callback, "r") as file:
                self.data = json.load(file)

        Logger.info(self.name + ": Loaded data")

    def _save(self, out):
        with open(self.save_path, "w", encoding='utf-8') as file:
            json.dump(out, file, ensure_ascii=True, indent=4)

        Logger.info(self.name + ": Saved data")

    def save(self):
        self._save(self.data)

    def create_new(self):
        open(self.save_path, "a").close()
        Logger.info(self.name + ": Created new data file")
        self._save(self.Default_data)

    def set(self, key, value):
        if key in self.data:
            self.data[key] = value

            Logger.info(self.name + ": Set " + str(key) + " to " + str(value))

        else:
            Logger.warn(self.name + ": \"" + str(key) + "\" is an invalid key")

    def get(self, key):
        if key in self.data:
            return self.data[key]

        else:
            Logger.warn(self.name + ": \"" + str(key) + "\" is an invalid key")


class _Globals:
    width = 0
    height = 0
    app = None

    def __init__(self):
        self.User_data = self._User_data()
        self.Settings_data = self._Settings_data()
        self.Textures = self._Textures()
        self.Audio = self._Audio()
        self.BuildingTextures = self._BuildingTextures()

    def get_screen_manager(self):
        return self.app.baseScreenManager.children[0]

    class _User_data(_user_and_settings_data_base):
        name = "User_Data"
        Default_data = {
            "introFinished": 0,
            "timesCrashed": 0,
            "building_layout": {
                "0": {
                    "name": "Rocket",
                    "data": {
                        "isBuilt": False
                    },
                    "center": [
                        50,
                        50
                    ],
                    "rotation": 0
                }
            }
        }

    class _Settings_data(_user_and_settings_data_base):
        name = "Settings_data"
        Default_data = {
            "buttonSize": 100
        }

    class GameSettings:
        # Where_Screen_What

        intro_ship_star_amount = 10
        intro_ship_star_width_divider = 10
        intro_ship_star_height_divider = 100
        intro_ship_star_new_frame_delay = 0.1
        intro_ship_ship_shake_amount_divider = 5
        intro_ship_ship_shake_delay = 4.75
        intro_ship_ship_shake_shake_length_times = (0.1, 0.05, 0.1)
        intro_ship_ship_new_frame_delay = 0
        intro_ship_ship_shake_positions = ((1, 0.5), (1, 0.5))
        intro_ship_alarm_color = 1, 0, 0, 0.5
        intro_ship_alarm_delay = 5.1
        intro_ship_alarm_switch_interval = 0.6
        intro_ship_alarm_sound_delay = 5
        intro_ship_alarm_sound_interval = 1.2
        intro_ship_alarm_sound_stop_delay = 9
        intro_ship_meteor_delay = 4
        intro_ship_meteor_length_times = (0, 0.25, 0.25, 0.25, 0.1)
        intro_ship_meteor_positions = ((0.75, 0.5), (0.75, 0.5), (0.75, 0.5), (0.75, 0.5), (1.2, 1.2))
        intro_ship_meteor_sizes = ((0, 0), (0.1, 0.1), (0.25, 0.25), (0.5, 0.5), (0.4, 0.4))
        intro_ship_meteor_hit_sound_delay = 4.5
        intro_ship_ship_fall_delay = 10
        intro_ship_ship_fall_sound_delay = 10
        intro_ship_ship_fall_speed = 1
        intro_ship_end_delay = 11

        intro_crash_move_delay = 0
        intro_crash_move_length = 2
        intro_crash_stars_move_divider = 3
        intro_crash_guide_delay = 3
        intro_crash_guide_speed = 1
        intro_crash_click_1_delay = 4
        intro_crash_click_transition_speed = 0.5

        base_builder_max_zoom = 3
        base_builder_min_zoom = 1
        base_builder_zoom_per_scroll = 0.1
        base_builder_default_zoom = 2
        base_builder_button_isBigger_amount = 2
        base_builder_new_frame_delay = 0

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

    class _BuildingTextures:
        _loaded_textures = {}
        _loaded_texture_infos = {}

        def _load_texture_infos(self, name):
            with open(str(os.path.join(str(os.path.split(str(get_Globals().app.directory))[0]), "resources", "3D", name,
                                       "textureInfo.json")), "r") as file:
                self._loaded_texture_infos[name] = json.load(file)

        def _load_texture(self, name, state, frame):
            frame = ("000" + str(frame))[-4:]

            self._loaded_textures[name + "/" + state + "/" + frame] = CoreImage(
                str(os.path.join(str(os.path.split(str(get_Globals().app.directory))[0]), "resources", "3D", str(name),
                                 str(state), str(frame) + ".png")))

        def get_texture_infos(self, name):
            if name not in self._loaded_texture_infos:
                self._load_texture_infos(name)

            return self._loaded_texture_infos[name]

        def get_texture(self, name, data, frame):
            textureInfo = self.get_texture_infos(name)
            state = 0

            for s in textureInfo:
                if textureInfo[s]["data"] == data:
                    state = s
                    break

            if (str(name) + "/" + str(state) + "/" + str(("000" + str(frame))[-4:])) not in self._loaded_texture_infos:
                print(self._loaded_textures)
                self._load_texture(name, state, frame)
                print("1")

            print(self._loaded_textures)

            print(2)

            return self._loaded_textures[(str(name) + "/" + str(state) + "/" + str(("000" + str(frame))[-4:]))]

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
