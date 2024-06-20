import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = []

screen.listen()
screen.onkey(player.road_cross, "Up")

game_is_on = True
while game_is_on:

    if random.randint(1, 6) == 1:
        new_car = CarManager()
        cars.append(new_car)

    for car in cars:
        car.move_forward()
        #Detect collision with car
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()
            
        
    if player.ycor() > 280:
        player.reset_position()
        #Detect finish line collision
        scoreboard.level_increase()
        for car in cars:
            car.increase_speed()
            

    time.sleep(0.1)
    screen.update()
    
screen.exitonclick()


    
    
