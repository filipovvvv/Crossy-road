from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.level = 1
        self.goto(-290, 260)
        self.update_level()




    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=("Arial", 20, "bold"), align="left")

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.clear()
        self.write(f"GAME OVER", font=("Arial", 20, "bold"), align="left")
