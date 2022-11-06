from turtle import Turtle, Screen
from paddle import Paddle
from net import Net
from ball import Ball
from scoreboard import Scoreboard
import time

BOARD_DIMENSIONS=[ 800, 600 ]

screen = Screen()
screen.setup(width=BOARD_DIMENSIONS[0], height=BOARD_DIMENSIONS[1])
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

net = Net(BOARD_DIMENSIONS)

paddle1=Paddle(BOARD_DIMENSIONS, 1)
paddle2=Paddle(BOARD_DIMENSIONS, 2)
ball=Ball()
score_board=Scoreboard(BOARD_DIMENSIONS)

screen.listen() 
screen.onkey(key="Up", fun=paddle2.up)
screen.onkey(key="Down", fun=paddle2.down)
screen.onkey(key="z", fun=paddle1.up)
screen.onkey(key="s", fun=paddle1.down)

game_is_on=True
playing=2

while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()
    print("heading "  , ball.heading())
    if ball.xcor() < -BOARD_DIMENSIONS[0]/2+60 and ball.distance(paddle1.paddle)<50 and ball.heading()>90 and ball.heading()<270:
        ball.send_back(paddle1.paddle.ycor()-ball.ycor())
    if ball.xcor() > BOARD_DIMENSIONS[0]/2-60 and ball.distance(paddle2.paddle)<50 and (ball.heading()<90 or ball.heading()>270):
        ball.send_back(paddle2.paddle.ycor()-ball.ycor())

    print(paddle1.paddle.position())

    if abs(ball.ycor())>BOARD_DIMENSIONS[1]/2-10:
        ball.hit_the_wall()

    if ball.xcor()>BOARD_DIMENSIONS[0]/2:
        score_board.score_up(1)
        time.sleep(1)
        ball.first_launch(1)
    if ball.xcor()<-BOARD_DIMENSIONS[0]/2:
        score_board.score_up(2)
        time.sleep(1)
        ball.first_launch(2)

screen.exitonclick()