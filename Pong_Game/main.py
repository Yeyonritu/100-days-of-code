from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time 

turtle = Turtle()
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0)) 
pong_ball = Ball()
score = Scoreboard()
    
screen.listen()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(pong_ball.pace)
    screen.update()
    pong_ball.move()
    
#Detect collision with wall and bounce
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        #bounce
        pong_ball.bounce_y()

#Detect collision with right and left paddle 
    
    if pong_ball.distance(r_paddle) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(l_paddle) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()
        
#Detect when r_paddle misses        
    
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        score.l_point()

#Detect when l_paddle misses     
    
    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        score.r_point()
        
        
screen.exitonclick()




