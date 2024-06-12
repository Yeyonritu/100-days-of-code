from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("blue")

#Dashed Line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#Draw Triangle, square, pentagon, haxagon, heptagon, octagon, nonagon and decagon

# #Draw Triangle
# for i in range(3):
#     tim.right(120)
#     tim.forward(100)  

# #Draw Square   
# for i in range(4):
#     tim.color("red")
#     tim.right(90)
#     tim.forward(100) 
    
# #Draw Pentagon
# for i in range(5):
#     tim.color("black")
#     tim.right(72)
#     tim.forward(100)
    
# #Draw hexagon
# for i in range(6):
#     tim.color("green")
#     tim.right(60)
#     tim.forward(100)
    
# #Draw heptagon
# for i in range(7):
#     tim.color("brown")
#     tim.right(51.43)
#     tim.forward(100)

# #Draw hexagon
# for i in range(8):
#     tim.color("yellow")
#     tim.right(45)
#     tim.forward(100)
    
# #Draw Nonagon
# for i in range(9):
#     tim.color("violet")
#     tim.right(40)
#     tim.forward(100)
    
# #Draw Decagon
# for i in range(10):
#     tim.color("pink")
#     tim.right(36)
#     tim.forward(100)

colours = ["red", "blue", "green"]
directions = [0, 90, 180, 270]


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
        
# for shape_side in range(3, 10 + 1):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side)
        
for random_movement in range(150):
    tim.pensize(10)
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.speed(10)

screen = Screen()
screen.exitonclick()