from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.goto(0,-280)
        self.color("white")
        self.up()
        self.setheading(90)



    def move_forward(self):
        self.setheading(90)
        self.forward(10)

