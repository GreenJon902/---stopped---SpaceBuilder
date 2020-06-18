from kivy import Logger
from kivy.uix.widget import Widget


class BaseScreenManager(Widget):
    def __init__(self, widget1, widget2):
        super(BaseScreenManager, self).__init__()
        self.widget1 = widget1
        self.widget2 = widget2

        self.add_widget(widget1)

    def next(self):
        self.clear_widgets()
        self.add_widget(self.widget2())

        Logger.info("Application: Starting App")
