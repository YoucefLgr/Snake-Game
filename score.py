from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.high = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100, 270)
        self.speed("fastest")
        self.plus()

    def plus(self):
        self.clear()
        with open("data.txt", mode="r") as file:
            x = file.read()
            self.write(f"Score :{self.x}   High Score : {x}", align="left", font=("Arial", 15, "normal"))

    def hi(self):
        if self.x > self.high:
            self.high = self.x
            with open("data.txt", mode="w") as file:
                file.write(str(self.high))
        self.x = 0
        self.plus()

    def increase(self):
        self.x += 1
        self.plus()
