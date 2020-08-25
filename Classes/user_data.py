from Classes.user_and_settings_data_base import user_and_settings_data_base


class User_data(user_and_settings_data_base):
    name = "User_Data"
    Default_data = {
        "introFinished": 0,
        "timesCrashed": 0,
        "building_layout": {
            "0": {
                "name": "rocket",
                "data": {
                    "isBuilt": False
                },
                "center": [
                    50,
                    50
                ],
                "rotation": 0
            }
        }
    }
