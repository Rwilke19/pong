from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = .1
        self.y_move = .1

    def move_ball(self):
        y_cor = self.ycor()
        x_cor = self.xcor()
        self.sety(y=y_cor + self.y_move)
        self.setx(x=x_cor + self.x_move)

    def wall_bounce(self):
        self.y_move *= -1

    def hit_paddle(self):
        self.x_move *= -1
