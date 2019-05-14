from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class Paddle(Widget):
    score = NumericProperty()

    def bounce(self, ball):
        if self.collide_widget(ball):
            velo_x, velo_y = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * velo_x, velo_y)
            velo = bounced * 1.1
            ball.velocity = velo.x, velo.y + offset


class Ball(Widget):
    x_axis_velocity = NumericProperty(0)
    y_axis_velocity = NumericProperty(0)

    velocity = ReferenceListProperty(x_axis_velocity, y_axis_velocity)

    def move_ball(self):
        self.pos = Vector(*self.velocity) + self.pos


class Game(Widget):
    ball = ObjectProperty(None)
    p1 = ObjectProperty(None)
    p2 = ObjectProperty(None)

    def serve_ball(self, velo=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = velo

    def update(self, dt):
        self.ball.move_ball()

        self.p1.bounce(self.ball)
        self.p2.bounce(self.ball)

        if(self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.y_axix_velocity *= -1

        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.x_axis_velocity *= -1

        if self.ball.x < self.x:
            self.p2.score += 1
            self.serve_ball(velo=(4, 0))

        if self.ball.x > self.width:
            self.p1.score += 1
            self.serve_ball(velo=(4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.p1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.p2.center_y = touch.y


class GameApp(App):
    def build(self):
        game = Game()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    GameApp().run()
