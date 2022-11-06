from turtle import Turtle

ALIGNEMENT= "center"
FONT = ("Arial",30,"normal")

class Scoreboard():
    def __init__(self, board_dimensions) -> None:
        self.board_dimensions = board_dimensions
        self.scores=[0,0]
        self.scoresObj=[Turtle(),Turtle()]
        self.initDisplay()
        self.display_scores()

    def initDisplay(self):
        for i, scoreObj in enumerate(self.scoresObj):
            side = -1 if i==0 else 1
            scoreObj.color("white")
            scoreObj.shapesize(0.1, 0.1)
            scoreObj.penup()
            scoreObj.goto(30*side,self.board_dimensions[1]/2-50 )

    def display_scores(self):
        for i,scoreObj in enumerate(self.scoresObj):
            side = -1 if i==0 else 1
            text_side= "right" if i==0 else "left"
            scoreObj.clear()
            scoreObj.goto(30*side,self.board_dimensions[1]/2-50 )
            scoreObj.write(f'{self.scores[i]}', True, align=text_side, font=FONT)

    def score_up(self,player):
        self.scores[player-1]+=1
        self.display_scores()
        