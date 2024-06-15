from turtle import Turtle
ASSEMBLY_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
SNAKE_AMOUNT = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) :
        
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for index in range(0, SNAKE_AMOUNT):
            new_snake = Turtle(shape = "square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(x = ASSEMBLY_POSITIONS[index], y = 0)
            self.segments.append(new_snake)
        
            
    def move(self):
        """Method that lets the snake to move by exchanging the first snake with the last one"""
        for seg in range(len(self.segments) - 1, 0, -1,):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor() 
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
                
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
                
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
        
        
        
        