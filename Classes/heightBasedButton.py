from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout

from Classes.globals import get_Globals
from Classes.postInitClass import PostInitClass


class HeightBasedButton(FloatLayout, PostInitClass):
    texture = StringProperty(deafaultvalue="")
    sendTo = StringProperty(deafaultvalue="baseBuilderScreen")

    def __init__(self, *args, **kwargs):
        super(HeightBasedButton, self).__init__(*args, **kwargs)

        self.Globals = get_Globals()
        self.image = None
        self.imageHolder = None
        self.size_hint = None, None

    def post_init(self):
        self.image = self.ids["image"]
        self.imageHolder = self.ids["imageHolder"]

        self.image.texture = self.Globals.Textures.__dict__[str(self.texture) + "_button"]

        self.size = self.height * (self.image.width / self.image.height), self.height

        self.image.size = self.size




    def on_touch_up(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.Globals.get_screen_manager().sendTo(self.sendTo)



