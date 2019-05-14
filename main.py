from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class Ball(Widget):
    x_axis_velocity = NumericProperty()
    y_axis_velocity = NumericProperty()

    velocity = ReferenceListProperty(x_axis_velocity, y_axis_velocity)

    def move_ball(self):
        self.pos = Vector(*self.velocity) + self.pos


class Game(Widget):
    ball = ObjectProperty(None)

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move_ball()

        if(self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.y_axix_velocity *= -1

        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.x_axis_velocity *= -1


class GameApp(App):
    def build(self):
        game = Game()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    GameApp().run()
