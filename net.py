from turtle import Turtle
class Net(Turtle):
    def __init__(self, board_dimensions) -> None:
        super().__init__()
        self.height=board_dimensions[1]
        self.dashes=[]
        self.dashes_init()

    def dashes_init(self):
        bottom = - self.height/2
        while bottom < self.height / 2:
            dash = []
            for d in range(2):
                d = Turtle()
                d.shape("square")
                d.penup()
                d.color("white")
                d.turtlesize(0.8,0.2)
                d.goto(0,bottom)
                dash.append(d)
                bottom += 20
            bottom += 30
            self.dashes.append(dash)
                        
