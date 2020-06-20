import os

from kivy import Logger
from kivy.core.window import Window
from kivy.lang import Builder

from Classes.globals import Globals


def add_user_data_save_paths(app):
    app.Globals.User_data.save_path = str(os.path.join(str(app.user_data_dir), "user_data.json"))

    Logger.info("Loader: Added user_data paths")


def add_settings_data_save_paths(app):
    app.Globals.Settings_data.save_path = str(os.path.join(str(app.user_data_dir), "settings_data.json"))

    Logger.info("Loader: Added settings_data paths")


def create_Globals(app):
    app.Globals = Globals()
    Logger.info("Loader: Created Globals")


def set_Globals_size(app):
    app.Globals.width = Window.width
    app.Globals.height = Window.height

    Logger.info("Loader: Added Globals window size")


def load_kv(app):
    Builder.load_file('kv.kv')

    Logger.info("Loader: Loaded KV")


def load_textures(app):
    app.Globals.Textures.load()

    Logger.info("Loader: Loaded Textures")


def append(bus):
    bus.append(("Loading KV", load_kv))
    bus.append(("Create Globals", create_Globals))
    bus.append(("Added Globals window size vars", set_Globals_size))
    bus.append(("Adding user data save paths", add_user_data_save_paths))
    bus.append(("Adding settings data save paths", add_settings_data_save_paths))
    bus.append(("Loading Textures", load_textures))

    return bus
