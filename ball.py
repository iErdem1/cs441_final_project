from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector


class Ball(Widget):
    x_axis_velocity = NumericProperty()
    y_axis_velocity = NumericProperty()

    velocity = ReferenceListProperty(x_axis_velocity, y_axis_velocity)

    def move_ball(self):
        self.pos = Vector(*self.velocity) + self.pos
