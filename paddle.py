from turtle import Turtle

DISTANCE_BEHIND_PADDLE = 30

class Paddle():
    def __init__( self, board_dimensions, player ) -> None:
        self.player= -1 if player==1 else 1
        self.board_dimensions = board_dimensions
        
        self.start_positions=[]
        self.init_start_position()

        self.paddle=[]
        self.init_barre()
        

    def init_barre(self):
        for sq in self.start_positions:
            square=Turtle()
            square.shape( "square" )
            square.color( "white" )
            square.penup()
            square.goto( *sq )
            self.paddle.append(square)

    def init_start_position(self):
        y= [40,20,0,-20,-40]
        for i in range(5):
            x_coord = ( self.board_dimensions[0] / 2 - DISTANCE_BEHIND_PADDLE ) * self.player
            print("x_coord : ", x_coord)
            y_coord = y[i]
            self.start_positions.append( [x_coord, y_coord] )
        print("b")
            
    def up(self):
        y_max=self.board_dimensions[1]/2
        if self.paddle[0].ycor() < y_max-20:
            for sq in self.paddle:
                sq.setheading(90)
                sq.forward(20)

    def down(self):
        y_max=-self.board_dimensions[1]/2
        if self.paddle[0].ycor() < -y_max+20:
            for sq in self.paddle:
                sq.setheading(270)
                sq.forward(20)


