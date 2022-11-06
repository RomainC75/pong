from turtle import Turtle

DISTANCE_BEHIND_PADDLE = 30

class Paddle():
    def __init__( self, board_dimensions, player ) -> None:
        self.player= -1 if player==1 else 1
        self.board_dimensions = board_dimensions
        self.paddle=Turtle()
        self.init_barre()
        

    def init_barre(self):
        self.paddle.shape( "square" )
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.color( "white" )
        self.paddle.penup()
        self.paddle.goto( self.player*(self.board_dimensions[0]/2-DISTANCE_BEHIND_PADDLE), 0 )
        

    


    def up(self):
        y_max=self.board_dimensions[1]/2
        if self.paddle.ycor() < y_max-60:
            self.paddle.goto(self.paddle.xcor(),self.paddle.ycor()+20)
            


    def down(self):
        y_min=-self.board_dimensions[1]/2
        if self.paddle.ycor() > y_min+60:
            self.paddle.goto(self.paddle.xcor(),self.paddle.ycor()-20)

