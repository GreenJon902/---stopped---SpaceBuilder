from kivy import properties


class Global:
    save_path = properties.StringProperty()

    class User_data:
        @classmethod
        def load(cls):
            print("load")
