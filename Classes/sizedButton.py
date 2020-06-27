from kivy.core.image import Texture
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.uix.floatlayout import FloatLayout

from Classes.globals import get_Globals
from Classes.postInitClass import PostInitClass


class SizedButton(FloatLayout, PostInitClass):
    isBig = BooleanProperty(defaultvalue=False)
    texture = ObjectProperty(deafaultvalue=Texture())

    def __init__(self, *args, **kwargs):
        super(SizedButton, self).__init__(*args, **kwargs)

        self.Globals = get_Globals()
        self.image = None


    def post_init(self):
        self.image = self.ids["image"]

        self.image.texture = self.texture

        if self.isBig:
            self.size_hint = (self.Globals.Settings_data.get("buttonSize") / 100) * 4

        else:
            self.size_hint = self.Globals.Settings_data.get("buttonSize") / 100


