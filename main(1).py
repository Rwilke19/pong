from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import random
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=300)
screen.title("Pong")
screen.tracer(0)

r_score = 0
l_score = 0
max_score_r = 10
max_score_l = 10
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score_title = Scoreboard((0, 130), "Score")
left_score = Scoreboard((-50, 120), f'{l_score}')
right_score = Scoreboard((50, 120), f'{r_score}')


screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move_ball()
    if ball.ycor() > 130 or ball.ycor() < -130:
        ball.wall_bounce()
    #Right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >= 340:
        ball.hit_paddle()
    #Left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() <= -340:
        ball.hit_paddle()
    if ball.distance(r_paddle) > 50 and ball.xcor() > 350:
        ball.goto(0, 0)
        l_score += 1
        left_score.update(f'{l_score}')
        max_score_l = max_score_l - 1
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)
    if ball.distance(l_paddle) > 50 and ball.xcor() < -350:
        ball.goto(0, 0)
        r_score += 1
        right_score.update(f'{r_score}')
        max_score_r = max_score_r - 1
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)
    if max_score_r == 0:
        score_title.update("The right side wins!")
        game_is_on = False
    if max_score_l == 0:
        score_title.update("The left side wins!")
        game_is_on = False



screen.exitonclick()
