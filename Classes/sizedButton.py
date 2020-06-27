from kivy import Logger
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout

from Classes.postInitClass import PostInitClass


class SizedButton(FloatLayout, PostInitClass):
    buttonId = StringProperty(defaultvalue="None")

    def __init__(self, *args, **kwargs):
        super(SizedButton, self).__init__(*args, **kwargs)

        self.image = None


    def post_init(self):
        self.image = self.ids["image"]

        self.bind(buttonId=self.idChange)
        self.idChange(None, str(self.buttonId))

    def idChange(self, _, value):
        print(_, value)
        if value == "None":
            Logger.warn("Application: SizedButton's id cannot be None")

            self.opacity = 0

        else:
            self.opacity = 1

