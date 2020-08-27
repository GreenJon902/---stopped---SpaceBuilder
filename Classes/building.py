from kivy.graphics import *
from kivy.properties import NumericProperty, StringProperty, DictProperty, BooleanProperty
from kivy.uix.widget import Widget

from Classes.globals import get_Globals


class Building(Widget):
    rotation = NumericProperty(0)
    frame = NumericProperty(0)
    frameStep = NumericProperty(1)
    lastFrame = NumericProperty(0)
    name = StringProperty("BuildingBase")
    data = DictProperty({})
    animated = BooleanProperty(False)
    rotatable = BooleanProperty(False)

    def __init__(self, *args, **kwargs):
        super(Building, self).__init__(*args, **kwargs)
        self.Globals = get_Globals()

        size = self.Globals.width / self.Globals.GameSettings.base_builder_building_size_divider
        self.size = size, size

        state = str(0)
        textureInfo = self.Globals.BuildingTextures.get_texture_info(self.name)
        for s in textureInfo:
            if textureInfo[s]["data"] == self.data:
                state = str(s)
                break

        self.frameStep = textureInfo[state]["frameStep"]
        self.lastFrame = textureInfo[state]["lastFrame"]
        self.animated = textureInfo[state]["animated"]
        self.rotatable = textureInfo[state]["rotatable"]

        self.Globals.BuildingSelectionHandler.register_building(self)

    def draw(self):
        self.canvas.clear()
        with self.canvas:
            Rectangle(pos=self.pos, size=self.size,
                      texture=self.Globals.BuildingTextures.get_texture(self.name, self.data, self.frame,
                                                                        self.rotation))

        if self.animated:
            self.frame += self.frameStep

            if self.frame > self.lastFrame:
                self.frame = 0

    def on_touch_up(self, touch):
        if touch.is_mouse_scrolling:
            return
        if not self.collide_point(touch.x, touch.y):
            return

        self.Globals.BuildingSelectionHandler.select_me(self)

    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            return
        if not self.collide_point(touch.x, touch.y):
            return
        if not self.Globals.BuildingSelectionHandler.am_i_selected(self):
            return
        print("mehehemove")



    def unselect(self):
        pass
