from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_input = screen.textinput(title = "Make ur bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
racers = []


for index in range(0, 6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[index])
    racers.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    
    
    for racer in racers:
        if racer.xcor() > 230:
            is_race_on = False
            winning_turtle = racer.pencolor()
            
            if winning_turtle == user_input:
                print(f"You win!, {winning_turtle} was right")
                
            else:
                print(f"You lose!, {winning_turtle} is the winner")
            
        forward_march = random.randint(0, 10)
        racer.forward(forward_march)
    

screen.exitonclick()

#Higher Order Functions i.e. function in function.
#W= forward, S = backward, A = left , D = right, c = clear screen

# def move_forward():
#     new_turtle.forward(50)
    
# def move_backward():
#     new_turtle.backward(50)

# def counter_clockwise():
#     new_turtle.left(50)

# def clockwise():
#     new_turtle.right(50)

# def clear_screen():
#     new_turtle.clear()
#     new_turtle.penup()
#     new_turtle.home()
#     new_turtle.pendown()

# screen.listen()
# screen.onkey(key = "w", fun = move_forward)
# screen.onkey(key = "s", fun = move_backward)
# screen.onkey(key = "a", fun = counter_clockwise)
# screen.onkey(key = "d", fun = clockwise)
# screen.onkey(key = "c", fun = clear_screen)