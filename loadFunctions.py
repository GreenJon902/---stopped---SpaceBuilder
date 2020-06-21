import os

from kivy import Logger
from kivy.core.window import Window
from kivy.lang import Builder

from Classes.globals import Globals


def add_save_paths(app):
    app.Globals.User_data.save_path = str(os.path.join(str(app.user_data_dir), "user_data.json"))
    app.Globals.Settings_data.save_path = str(os.path.join(str(app.user_data_dir), "settings_data.json"))

    Logger.info("Loader: Added save paths")


def create_Globals(app):
    app.Globals = Globals()

    app.Globals.width = Window.width
    app.Globals.height = Window.height

    Logger.info("Loader: Created Globals")


def load_kv(app):
    Builder.load_file('kv.kv')

    Logger.info("Loader: Loaded KV")


def load_textures(app):
    app.Globals.Textures.load()

    Logger.info("Loader: Loaded Textures")


def load_audio(app):
    app.Globals.Audio.load()

    Logger.info("Loader: Loaded Audio")
