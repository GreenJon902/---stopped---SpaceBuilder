from kivy.uix.floatlayout import FloatLayout

from Classes.postInitClass import PostInitClass


class SizedButton(FloatLayout, PostInitClass):
    def __init__(self, *args, **kwargs):
        super(SizedButton, self).__init__(*args, **kwargs)

        self.image = None

    def post_init(self):
        self.image = self.ids["image"]
