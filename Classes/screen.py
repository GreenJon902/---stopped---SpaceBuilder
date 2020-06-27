from kivy.clock import Clock
from kivy.uix.screenmanager import Screen as _Screen

from Classes.postInitClass import PostInitClass


class Screen(_Screen, PostInitClass):
    def on_enter(self, *args, **kwargs):
        super(Screen, self).__init__(*args, **kwargs)

        Clock.schedule_once(lambda x: self.post_enter(), 0)

    def post_enter(self):
        pass


