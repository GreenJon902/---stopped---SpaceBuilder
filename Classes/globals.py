import json

from kivy.event import EventDispatcher
from kivy.properties import StringProperty, Property, NumericProperty
from kivy.logger import Logger


class Globals:
    width = 0
    height = 0

    def __init__(self):
        self.User_data = self._User_data()
        self.Settings_data = self._Settings_data()

    class _User_data(EventDispatcher):
        Default_data = {
            "intoFinished": 0,
            "timesCrashed": 0,
            "layout": {}
        }

        save_path = StringProperty()
        data = {}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.bind(save_path=self.load)

        def load(self, _, callback):
            Logger.info("Application: App data save path: " + str(callback))

            try:
                with open(callback, "r") as file:
                    self.data = json.load(file)

            except FileNotFoundError:
                Logger.warn("Application: User data save file not found, creating new one")
                self.create_new()

                with open(callback, "r") as file:
                    self.data = json.load(file)

            Logger.info("Application: Loaded user data")

        def save(self, out):
            with open(self.save_path, "w", encoding='utf-8') as file:
                json.dump(out, file, ensure_ascii=True, indent=4)

            Logger.info("Application: Saved user data")

        def create_new(self):
            open(self.save_path, "a").close()
            Logger.info("Application: Created new user data file")
            self.save(self.Default_data)

        def set(self, key, value):
            if key in self.data:
                self.data[key] = value

            else:
                Logger.warn("Application: \"" + str(key) + "\" is an invalid key for User data")

        def get(self, key):
            if key in self.data:
                return self.data[key]

            else:
                Logger.warn("Application: \"" + str(key) + "\" is an invalid key for User data")

    class _Settings_data(EventDispatcher):
        Default_data = {
            "buttonSize": 10
        }

        save_path = StringProperty()
        data = {}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.bind(save_path=self.load)

        def load(self, _, callback):
            Logger.info("Application: App data save path: " + str(callback))

            try:
                with open(callback, "r") as file:
                    self.data = json.load(file)

            except FileNotFoundError:
                Logger.warn("Application: Settings data save file not found, creating new one")
                self.create_new()

                with open(callback, "r") as file:
                    self.data = json.load(file)

            Logger.info("Application: Loaded settings data")

        def save(self, out):
            with open(self.save_path, "w", encoding='utf-8') as file:
                json.dump(out, file, ensure_ascii=True, indent=4)

            Logger.info("Application: Saved settings data")

        def create_new(self):
            open(self.save_path, "a").close()
            Logger.info("Application: Created new settings data file")
            self.save(self.Default_data)

        def set(self, key, value):
            if key in self.data:
                self.data[key] = value

            else:
                Logger.warn("Application: \"" + str(key) + "\" is an invalid key for Settings data")

        def get(self, key):
            if key in self.data:
                return self.data[key]

            else:
                Logger.warn("Application: \"" + str(key) + "\" is an invalid key for Settings data")

