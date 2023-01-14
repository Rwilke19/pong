from turtle import Turtle
LENGTH_FACTOR = 5
Y_COR = 0

class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=LENGTH_FACTOR)
        self.penup()
        self.goto(xcor, ycor)
        self.setheading(90)


    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)

