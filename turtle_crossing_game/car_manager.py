from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__ (self):
        super().__init__()
        self.allcars = []
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid = 1, stretch_len = 2)
        self.penup()
        x_pos = 300
        y_pos = random.randint(-250, 250)
        self.goto(y = y_pos, x = x_pos)
        self.setheading(180)
        self.initial_speed = STARTING_MOVE_DISTANCE
        
        
    def move_forward(self):
        
        self.forward(self.initial_speed)
        
    def increase_speed(self):
        self.initial_speed += MOVE_INCREMENT
        
        
        
