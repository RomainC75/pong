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
playing=1

while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    targetPaddle= paddle2 if playing==1 else paddle1
    for i, sq in enumerate(targetPaddle.paddle):
        if ball.distance(sq)<=22:
            hit_position = targetPaddle.get_center_ycor()-ball.ycor()
            ball.send_back(hit_position)
            playing = 2 if playing==1 else 1
    
    if abs(ball.ycor())>BOARD_DIMENSIONS[1]/2-10:
        ball.hit_the_wall()

    if abs(ball.xcor())>BOARD_DIMENSIONS[0]/2:
        score_board.score_up(playing)
        time.sleep(1)
        ball.first_launch(playing)


screen.exitonclick()