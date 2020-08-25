import json

from kivy import Logger
from kivy.event import EventDispatcher
from kivy.properties import StringProperty


class user_and_settings_data_base(EventDispatcher):
    Default_data = {}
    save_path = StringProperty()
    data = {}
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bind(save_path=self.load)

    def load(self, _, callback):
        Logger.info(self.name + ": Save path: " + str(callback))

        try:
            with open(callback, "r") as file:
                self.data = json.load(file)

        except FileNotFoundError:
            Logger.warn(self.name + ": Save file not found, creating new one")
            self.create_new()

            with open(callback, "r") as file:
                self.data = json.load(file)

        Logger.info(self.name + ": Loaded data")

    def _save(self, out):
        with open(self.save_path, "w", encoding='utf-8') as file:
            json.dump(out, file, ensure_ascii=True, indent=4)

        Logger.info(self.name + ": Saved data")

    def save(self):
        self._save(self.data)

    def create_new(self):
        open(self.save_path, "a").close()
        Logger.info(self.name + ": Created new data file")
        self._save(self.Default_data)

    def set(self, key, value):
        if key in self.data:
            self.data[key] = value

            Logger.info(self.name + ": Set " + str(key) + " to " + str(value))

        else:
            Logger.warn(self.name + ": \"" + str(key) + "\" is an invalid key")

    def get(self, key):
        if key in self.data:
            return self.data[key]

        else:
            Logger.warn(self.name + ": \"" + str(key) + "\" is an invalid key")