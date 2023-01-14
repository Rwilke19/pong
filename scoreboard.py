from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position, words):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.pendown()
        self.write(words, move=False, align="center")

    def update(self, words):
        self.clear()
        self.write(words, move=False, align="center")
