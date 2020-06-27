from kivy.clock import Clock


class PostInitClass:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        Clock.schedule_once(lambda x: self.post_init(), 0)

    def post_init(self):
        pass
