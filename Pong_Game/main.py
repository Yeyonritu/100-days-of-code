from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time 

turtle = Turtle()
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

#time = time()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0)) 
pong_ball = Ball()
    
screen.listen()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.3)
    screen.update()
    pong_ball.move()
    

screen.exitonclick()




