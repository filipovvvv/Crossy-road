import random
from turtle import Turtle
class Cars:
    def __init__(self):
        self.cars = []
        self.last_created_car = None
        self.move_speed = 0.1
        self.colors = ["green","red","blue","gray","brown"]



    def create_car(self):
        car = Turtle()
        car.color(random.choice(self.colors))
        car.up()
        car.shape("square")
        car.speed("slow")
        car.shapesize(stretch_wid=1, stretch_len=5)
        car.goto(280, random.randint(-250, 250))
        car.setheading(180)
        self.cars.append(car)
        self.last_created_car = car

    def create_cars(self):
        if self.last_created_car.xcor() < 150:
            self.create_car()

    def move_forward(self):
        for car in self.cars:
            car.forward(10)

    def move_faster(self):
        self.move_speed *= 0.2


