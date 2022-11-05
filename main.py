from turtle import Turtle, Screen
from paddle import Paddle
from net import Net
import time

BOARD_DIMENSIONS=[ 800, 600 ]

screen = Screen()
screen.setup(width=BOARD_DIMENSIONS[0], height=BOARD_DIMENSIONS[1])
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

paddle1=Paddle(BOARD_DIMENSIONS, 1)
paddle2=Paddle(BOARD_DIMENSIONS, 2)

net = Net(BOARD_DIMENSIONS)

screen.listen() 
screen.onkey(key="Up", fun=paddle2.up)
screen.onkey(key="Down", fun=paddle2.down)
screen.onkey(key="z", fun=paddle1.up)
screen.onkey(key="s", fun=paddle1.down)

game_is_on=True


while game_is_on:
    screen.update()
    time.sleep(0.001)


screen.exitonclick()