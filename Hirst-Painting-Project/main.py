from turtle import Turtle, Screen
import random
relevant_color = [(229, 228, 226), (225, 223, 225), (199, 175, 117), (212, 222, 215), (125, 36, 24), (223, 224, 228), (167, 106, 56), 
                  (186, 159, 52), (6, 57, 83), (108, 68, 85), (112, 161, 175), (21, 122, 174), (63, 153, 138), (39, 36, 35), 
                  (76, 40, 48), (9, 68, 47), (90, 141, 52), (182, 96, 79), (131, 38, 41), (141, 171, 156), (210, 200, 149), 
                  (179, 201, 186), (173, 153, 159), (212, 183, 176), (151, 114, 119)]
tim = Turtle()
screen = Screen()
screen.colormode(255)

tim.penup()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(relevant_color))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(100)
        tim.forward(500)
        tim.setheading(0)
    
screen.exitonclick()