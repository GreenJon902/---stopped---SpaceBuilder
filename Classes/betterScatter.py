from kivy.graphics.transformation import Matrix
from kivy.uix.scatter import ScatterPlane

from Classes.globals import get_Globals


class BetterScatter(ScatterPlane):
    def __init__(self, *args, **kwargs):
        super(BetterScatter, self).__init__(*args, **kwargs)

        self.Globals = get_Globals()

        self.scale_min = self.Globals.GameSettings.base_builder_min_zoom
        self.scale_max = self.Globals.GameSettings.base_builder_max_zoom


    def transform_with_touch(self, touch):
        changed = False

        if len(self._touches) == 1:
            xAdd = touch.pos[0] - self._last_touch_pos[touch][0]
            yAdd = touch.pos[1] - self._last_touch_pos[touch][1]

            left = self._get_x()
            bottom = self._get_y()
            right = self.get_right()
            top = self.get_top()

            dx = 0
            dy = 0

            if left + xAdd <= 0 and right + xAdd >= self.Globals.width:  # right,  left
                dx = xAdd

                changed = True

            if bottom + yAdd <= 0 and top + yAdd >= self.Globals.height:  # up, down
                dy = yAdd

                changed = True


            self.apply_transform(Matrix().translate(dx, dy, 0))


        else:

            changed = super(BetterScatter, self).transform_with_touch(touch)

        return changed


    def on_transform_with_touch(self, touch):
        (x, y), (w, h) = self.bbox

        dx = 0
        dy = 0

        if x > 0:
            dx = x * -1

        elif x < self.Globals.width:
            dx = (x * -1) - self.Globals.width

        if y > 0:
            dy = y * -1

        elif y < self.Globals.width:
            dy = (y * -1) * - self.Globals.height
