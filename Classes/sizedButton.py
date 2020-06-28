from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout

from Classes.globals import get_Globals
from Classes.postInitClass import PostInitClass


class SizedButton(FloatLayout, PostInitClass):
    isBig = BooleanProperty(defaultvalue=False)
    texture = StringProperty(deafaultvalue="")

    def __init__(self, *args, **kwargs):
        super(SizedButton, self).__init__(*args, **kwargs)

        self.Globals = get_Globals()
        self.image = None
        self.imageHolder = None
        self.size_hint = None, None

    def post_init(self):
        self.image = self.ids["image"]
        self.imageHolder = self.ids["imageHolder"]

        self.parent.width = self.Globals.Settings_data.get("buttonSize") * \
            self.Globals.GameSettings.base_builder_button_isBigger_amount

        self.image.texture = self.Globals.Textures.__dict__[str(self.texture) + "_button"]

        if self.isBig:
            self.size = self.Globals.Settings_data.get("buttonSize") * \
                        self.Globals.GameSettings.base_builder_button_isBigger_amount, \
                        self.Globals.Settings_data.get("buttonSize") * \
                        self.Globals.GameSettings.base_builder_button_isBigger_amount

            self.imageHolder.size = self.Globals.Settings_data.get("buttonSize") * \
                self.Globals.GameSettings.base_builder_button_isBigger_amount, \
                self.Globals.Settings_data.get("buttonSize") * \
                self.Globals.GameSettings.base_builder_button_isBigger_amount

            self.image.size = self.Globals.Settings_data.get("buttonSize") * \
                self.Globals.GameSettings.base_builder_button_isBigger_amount, \
                self.Globals.Settings_data.get("buttonSize") * \
                self.Globals.GameSettings.base_builder_button_isBigger_amount



        else:
            self.size = self.Globals.Settings_data.get("buttonSize") * \
                              self.Globals.GameSettings.base_builder_button_isBigger_amount, \
                              self.Globals.Settings_data.get("buttonSize")

            self.imageHolder.size = self.Globals.Settings_data.get("buttonSize"), \
                self.Globals.Settings_data.get("buttonSize")
            self.image.size = self.Globals.Settings_data.get("buttonSize"), self.Globals.Settings_data.get("buttonSize")

