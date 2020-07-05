from kivy.graphics.transformation import Matrix
from kivy.uix.scatter import ScatterPlane

from Classes.globals import get_Globals


class BetterScatter(ScatterPlane):
    def __init__(self, *args, **kwargs):
        super(BetterScatter, self).__init__(*args, **kwargs)

        self.Globals = get_Globals()

        self.scale_min = self.Globals.GameSettings.base_builder_min_zoom
        self.scale_max = self.Globals.GameSettings.base_builder_max_zoom
        self.scale = self.Globals.GameSettings.base_builder_default_zoom


    def on_transform_with_touch(self, touch):
        (x, y), (w, h) = self.bbox

        dx = 0
        dy = 0

        if x > 0:
            dx = 0 - x

        elif x + w < self.Globals.width:
            dx = self.Globals.width - (x + w)

        if y > 0:
            dy = 0 - y

        elif y + h < self.Globals.height:
            dy = self.Globals.height - (y + h)


        self.apply_transform(Matrix().translate(dx, dy, 0))
