from Classes.screen import Screen


class LoadingScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(LoadingScreen, self).__init__(*args, **kwargs)

        self.bus = list()

    def start_bus(self):
        for callback in self.bus:
            callback()
