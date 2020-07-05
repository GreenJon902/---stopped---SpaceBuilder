import os

from kivy import Logger
from kivy.core.window import Window
from kivy.lang import Builder

from Classes.globals import init, get_Globals


def add_save_paths(app):
    Globals = get_Globals()

    Globals.User_data.save_path = str(os.path.join(str(app.user_data_dir), "user_data.json"))
    Globals.Settings_data.save_path = str(os.path.join(str(app.user_data_dir), "settings_data.json"))

    Logger.info("Loader: Added save paths")


def create_Globals(app):
    init()
    Globals = get_Globals()

    Globals.width = Window.width
    Globals.height = Window.height
    Globals.app = app

    Logger.info("Loader: Created Globals")


def load_kv(app):
    Builder.load_file('resources/kv.kv')

    Logger.info("Loader: Loaded KV")


def load_textures(app):
    Globals = get_Globals()
    Globals.Textures.load()

    Logger.info("Loader: Loaded Textures")


def load_audio(app):
    Globals = get_Globals()
    Globals.Audio.load()

    Logger.info("Loader: Loaded Audio")
