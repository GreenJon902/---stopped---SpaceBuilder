from kivy.graphics.transformation import Matrix
from kivy.properties import BooleanProperty
from kivy.uix.scatter import ScatterPlane

from Classes.globals import get_Globals


class BetterScatter(ScatterPlane):
    scrollToZoom = BooleanProperty(False)

    def __init__(self, *args, **kwargs):
        super(BetterScatter, self).__init__(*args, **kwargs)

        self.Globals = get_Globals()

    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling and self.scrollToZoom:

            if touch.button == 'scrolldown':
                if self.scale < self.Globals.GameSettings.base_builder_max_zoom:

                    nextScale = self.scale * 1.1
                    if nextScale < self.Globals.GameSettings.base_builder_max_zoom:
                        self.scale = nextScale

                    else:
                        self.scale = self.Globals.GameSettings.base_builder_max_zoom

            elif touch.button == 'scrollup':
                if self.scale > self.Globals.GameSettings.base_builder_min_zoom:

                    nextScale = self.scale * 0.8
                    if nextScale > self.Globals.GameSettings.base_builder_min_zoom:
                        self.scale = nextScale

                    else:
                        self.scale = self.Globals.GameSettings.base_builder_min_zoom

            self.dispatch("on_transform_with_touch", None)

        else:
            super(BetterScatter, self).on_touch_down(touch)


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
