from turtle import Turtle
import random

BOUNCE_FACTOR=0.3
BASE_SPEED=3

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.first_launch(1)
        self.speed=3
                
    def first_launch(self,player):
        self.speed=BASE_SPEED
        self.setheading(0)
        self.goto(0,random.randrange(-180,180))
        self.left(random.randrange(-45,45))
        if player!=1:
            self.left(180)
        
    def move(self):
        self.forward(self.speed)

    def send_back(self,side_distance):
        bounce = BOUNCE_FACTOR*side_distance
        # print("bounce : ",bounce)
        attack_heading=self.heading()
        # print("attack heading : ", attack_heading)
        if attack_heading<=90:
            self.left(bounce)    
            self.right(attack_heading*2 )
            
        elif attack_heading>270:
            self.left(bounce)
            self.left( (360-attack_heading)*2 )
            
        elif attack_heading>90 and attack_heading<=180:
            self.right(bounce)
            self.left( (180-attack_heading)*2 )
            
        elif attack_heading>180 :
            self.right(bounce)
            self.right( (attack_heading-180)*2 )
    
        self.left(180)
        self.speed+=0.25
        
    def hit_the_wall(self):
        attack_heading=self.heading()
        if attack_heading<=90:
            self.right(attack_heading*2)
        elif attack_heading>270:
            self.left( (360-attack_heading)*2 )
        elif attack_heading>90 and attack_heading<=180:
            self.left( (180-attack_heading)*2 )
        elif attack_heading>180 :
            self.right( (attack_heading-180)*2 )
        

    def speed_up(self):
        self.speed+=1

    