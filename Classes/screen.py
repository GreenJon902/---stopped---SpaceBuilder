from kivy.clock import Clock
from kivy.uix.screenmanager import Screen as _Screen


class Screen(_Screen):
    def __init__(self, *args, **kwargs):
        super(Screen, self).__init__(*args, **kwargs)

    def on_enter(self, *args, **kwargs):
        super(Screen, self).__init__(*args, **kwargs)

        Clock.schedule_once(lambda x: self.post_init())

    def post_init(self):
        pass
