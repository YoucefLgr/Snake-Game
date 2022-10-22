from turtle import Turtle, Screen


TURTLES = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.turtles = []
        self.create()

    def create(self):
        for i in TURTLES:
            self.create_seg(i)

    def create_seg(self, i):
        seg = Turtle("square")
        seg.color("white")
        seg.speed("fastest")
        seg.penup()
        seg.goto(i)
        self.turtles.append(seg)

    def extend(self):
        self.create_seg(self.turtles[-1].position())

    def reset(self):
        for _ in self.turtles:
            _.goto(1000, 1000)
        self.turtles.clear()
        self.create()

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[i - 1].xcor()
            y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(x, y)
        self.turtles[0].forward(20)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)
