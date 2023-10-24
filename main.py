from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.tracer(0)
screen.title("PONG")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.listen()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

game_is_on = True

screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
scoreboard_l = ScoreBoard((-50, 250))
scoreboard_r = ScoreBoard((50, 250))
goal = int(input("What is the score to win?"))

while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()
    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.bounce()
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.change_direction()

    if ball.xcor() >= 385:
        scoreboard_l.increase_score()
        ball.origin()

    elif ball.xcor() <= -385:
        scoreboard_r.increase_score()
        ball.origin()

    if scoreboard_l.score >= goal or scoreboard_r.score >= goal:
        game_is_on = False


screen.exitonclick()
