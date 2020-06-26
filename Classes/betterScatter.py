from kivy.uix.scatter import Scatter

from Classes.globals import get_Globals


class BetterScatter(Scatter):
    def __init__(self, *args, **kwargs):
        super(BetterScatter, self).__init__(*args, **kwargs)

        self.scale_min = get_Globals().min_zoom
        self.scale_max = get_Globals().max_zoom
