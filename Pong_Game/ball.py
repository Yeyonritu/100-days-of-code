from turtle import Turtle
class Ball(Turtle):
    def __init__ (self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        #self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.pace = 0.1
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.y_move *= -1
        self.pace *= 0.9
        
    def bounce_x(self):
        self.x_move *= -1
        
    def reset_position(self):
        new_x = 0
        new_y = 0
        self.goto(new_x, new_y)
        self.bounce_x()
         