from kivy.clock import Clock
from kivy.uix.screenmanager import Screen


class Screen(Screen):
    def __init__(self, *args, **kwargs):
        super(Screen, self).__init__(*args, **kwargs)
        Clock.schedule_once(self._finish_init)

    def post_init(self, _):
        pass