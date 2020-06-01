from kivy.clock import Clock
from kivy.uix.screenmanager import Screen


class Screen(Screen):
    def __init__(self, *args, **kwargs):
        super(Screen, self).__init__(*args, **kwargs)
        Clock.schedule_once(lambda x: self.post_init())

    def post_init(self):
        pass
