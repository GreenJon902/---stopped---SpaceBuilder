import json
import os

from kivy.core.image import Image as CoreImage

from Classes.globals import get_Globals


class BuildingTextures:
    _loaded_textures = {}
    _loaded_texture_infos = {}

    def __init__(self):
        self.Globals = get_Globals()

    def _load_texture_infos(self, name):
        with open(str(os.path.join(str(os.path.split(str(self.Globals.app.directory))[0]), "resources", "3D", name,
                                   "textureInfo.json")), "r") as file:
            self._loaded_textures[name] = json.load(file)

    def _load_texture(self, name, state, frame):
        self._loaded_textures[name + "/" + state + "/" + frame] = CoreImage(
            str(os.path.join(str(os.path.split(str(self.Globals.app.directory))[0]), "resources", "3D", name, state,
                             frame)))

    def get_texture_infos(self, name):
        if name not in self._loaded_texture_infos:
            self._load_texture_infos(name)

        return self._loaded_textures_infos[name]

    def get_texture(self, name, data, frame):
        textureInfo = self.get_texture_infos(name)
        state = 0

        for s in textureInfo:
            if textureInfo[s]["data"] == data:
                state = s
                break

        if (name + "/" + state + "/" + frame) not in self._loaded_texture_infos:
            self._load_texture(name, state, frame)

        return self._loaded_textures[(name + "/" + state + "/" + frame)]
