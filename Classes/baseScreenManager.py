from kivy import Logger
from kivy.animation import Animation
from kivy.uix.widget import Widget


class BaseScreenManager(Widget):
    def __init__(self, widget1, widget2):
        super(BaseScreenManager, self).__init__()
        self.widget1 = widget1
        self.widget2 = widget2

        self.add_widget(widget1)

    def next(self):
        self.widget2 = self.widget2()

        ani = Animation(opacity=1, duration=0)
        ani += Animation(opacity=0, duration=1)
        ani.bind(on_complete=lambda x, x2: self.remove_widget(self.widget1))
        ani.start(self.widget1)

        self.add_widget(self.widget2)

        ani = Animation(opacity=0, duration=0)
        ani += Animation(opacity=1, duration=1)
        ani.start(self.widget2)

        Logger.info("Application: Starting App")
