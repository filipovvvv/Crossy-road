import turtle
from turtle import Screen
from player import Player
from cars import Cars
from level import Level
import time
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Crossy Road")
screen.tracer(0)

cars = Cars()
player = Player()
level = Level()


screen.listen()
screen.onkey(player.move_forward,"Up")
cars.create_car()


game_is_on = True
while game_is_on:
    cars.move_forward()
    time.sleep(cars.move_speed)
    cars.create_cars()



    for car in cars.cars:
        if player.distance(car) < 30:
            game_is_on = False
            level.game_over()




    if player.ycor() > 250:
        level.increase_level()
        player.goto(0,-280)
        cars.move_faster()




    screen.update()














screen.exitonclick()